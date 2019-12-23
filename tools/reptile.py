import requests
from bs4 import BeautifulSoup
import os
import re
import json
from lxml import html

bbs_url = 'https://bbs.pku.edu.cn/v2/post-read.php?bid=690&threadid=17467265'

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)


def remove_emoji(text):
    return emoji_pattern.sub(r'', text)


# header = {
#     'Referer': 'https://bbs.pku.edu.cn/v2/thread.php?bid=690',
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/79.0.3945.88 Mobile Safari/537.36'
# }

def get_reply(url, result_file):
    response = requests.get(url).text
    # print(response)
    # os._exit(0)
    soup = BeautifulSoup(response, 'lxml')
    max_reply_page = list(set(soup.find_all('input', attrs={'data-role': 'goto-input'})))[0]['max']

    title = str(soup.find_all('title')[0].get_text()).strip().split('-')[0]
    title = remove_emoji(title)
    print('帖子题目 = {}'.format(title))
    result_file.write(title.replace(u'\xa0', u'') + '\n')

    for reply_page in range(int(max_reply_page)):
        print('\t该帖回复{}页，正在提取第{}页'.format(max_reply_page, reply_page))
        page_url = url + '&page=' + str(reply_page+1)
        response = requests.get(page_url).text
        soup = BeautifulSoup(response, 'lxml')

        replies = soup.find_all('div', class_='body file-read image-click-view')
        for i, content in enumerate(replies):
            list_content = content.select('p')
            for item in list_content:
                text = str(item.get_text().strip())
                if text[:9] == 'Anonymous':
                    break
                text = remove_emoji(text)
                result_file.write(text.replace(u'\xa0', u'') + '\n')


def main():
    f = open('result.txt', 'a+', encoding='utf-8')
    for page in range(300):
        print('page {}/300....'.format(page), end=' ')
        directory_url = 'https://bbs.pku.edu.cn/v2/thread.php?bid=690&mode=topic&page=' + str(page)
        response = requests.get(directory_url).text
        soup = BeautifulSoup(response, 'lxml')
        items = soup.find_all('div', {'class': 'list-item-topic list-item'})

        # 该page有哪些帖子
        for item in items:
            thread_id = item['data-itemid']
            if int(thread_id) < 0:
                continue
            reply_url = 'https://bbs.pku.edu.cn/v2/post-read.php?bid=690&threadid=' + str(thread_id)

            # 进入到该帖子爬取回帖
            get_reply(reply_url, f)


if __name__ == '__main__':
    main()
