import requests
from bs4 import BeautifulSoup
import os
import time
import re
import random

proxy_list = ['183.146.213.157:80', '39.137.107.98:80', '39.137.69.7:8080',
              '113.128.24.101:9999', '39.137.69.9:8080', '117.88.177.48:3000']


def test_proxy(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }
    # print(url)
    import requests
    s = requests.session()
    # url = "https://www.douban.com"
    s.proxies = {"http": random.choice(proxy_list)}
    r = s.get(url, headers=headers).text
    return r


def filter_str(desstr, restr=''):
    # 过滤除中英文及数字以外的其他字符
    res = re.compile("[^\u4e00-\u9fa5-\uFF0C^a-z^A-Z^0-9]")
    return res.sub(restr, desstr)


def get_reply(url, result_file, cnt):
    response = test_proxy(url)
    # response = get_html(url)
    soup = BeautifulSoup(response, 'lxml')

    topic_content = soup.find_all('div', {'class': 'topic-richtext'})
    if len(topic_content):
        topic_content = topic_content[0].select('p')
    else:
        return
    result = ''
    for line in topic_content:
        if line.string:
            result += line.string
    # print(result, type(result))
    if len(result) != 0:
        # result_file.append([filter_str(result)])
        result_file.write(filter_str(result) + '\n')
        cnt += 1

    # print(response)
    user_replies = soup.select('p[class=reply-content]')
    for reply in user_replies:
        reply = reply.string
        if reply and type(reply) != 'bs4.element.NavigableString' and len(filter_str(reply)) >= 5:
            filter_reply = filter_str(reply)
            if len(filter_reply) >= 5:
                result_file.write(filter_str(reply) + '\n')
                cnt += 1


def check_line(file):
    with open(file, 'r') as f:
        print(len(f.readlines()))
    os._exit(0)


def optic_crawl(topic):
    # wb = Workbook()
    # ws = wb.create_sheet(title='douban')
    # check_line('./' + topic + '.txt')

    ws = open('./result/' + topic + '.txt', 'a+')
    print('====================================================')

    root_url = 'https://www.douban.com/group/' + topic + '/discussion?start=0'
    response = test_proxy(root_url)
    soup = BeautifulSoup(response, 'lxml')
    retry = 5
    while retry > 0 and len(soup.find_all('span', {'class': 'thispage'})) == 0:
        # print(response)
        print('rejected')
        response = test_proxy(root_url)
        soup = BeautifulSoup(response, 'lxml')
        retry -= 1
        return

    max_pages = int(soup.find_all('span', {'class': 'thispage'})[0].attrs['data-total-page'])

    print(max_pages)

    pages = list(range(max_pages, 1, -3))

    cnt = 0
    for i, page in enumerate(pages):
        if i >= 1:
            wait_sec = random.randint(180, 240)
            print('**** wait for {} min ****'.format(int(wait_sec/60)))
            time.sleep(wait_sec)
        time_start = time.time()

        directory_url = 'https://www.douban.com/group/' + topic + '/discussion?start=' + str(25 * page)
        response = test_proxy(directory_url)
        # response = requests.get(directory_url,
        #                         headers={'User-Agent': user_agent},
        #                         proxies=proxies, ).text
        soup = BeautifulSoup(response, 'lxml')
        items = soup.find_all('td', {'class': 'title'})

        # 该page有哪些帖子
        for item in items:
            href = item.select('a')[0].attrs['href']
            title = item.select('a')[0].attrs['title']

            # print(title)
            ws.write(filter_str(title + '\n'))
            cnt += 1
            reply_url = href

            # 进入到该帖子爬取回帖
            get_reply(reply_url, ws, cnt)
        time_end = time.time()
        print('page ', page, 'time cost', time_end - time_start, 's')
    # wb.save('./' + topic + '.xlsx')


def main():
    topics = {'职业发展': ['myjob', 'Dilbert521'], '恋爱关系': ['fanjianlove', '151793'],
              '学业方面': ['626766', 'hateschool'], '师生关系': ['evilteacher', 'BADTEACHER']}
    # topics = {'职业发展': ['myjob']}
    for topic in topics.keys():
        for group in topics[topic]:
            print(topic, group)
            optic_crawl(group)


if __name__ == '__main__':
    main()
