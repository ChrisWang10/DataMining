from bs4 import BeautifulSoup
import datetime
import requests
import json
import random

ip_random = -1
article_tag_list = []
article_type_list = []


def get_html(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    global ip_random
    ip_rand, proxies = get_proxie(ip_random)
    # print(proxies)
    try:
        request = requests.get(url=url, headers=header, proxies=proxies, timeout=3)
    except:
        request_status = 500
    else:
        request_status = request.status_code
    # print(request_status)
    while request_status != 200:
        ip_random = -1
        ip_rand, proxies = get_proxie(ip_random)
        # print(proxies)
        try:
            request = requests.get(url=url, headers=header, proxies=proxies, timeout=3)
        except:
            request_status = 500
        else:
            request_status = request.status_code
        # print(request_status)
    ip_random = ip_rand

    return request.text


def get_proxie(random_number):
    with open('ip.txt', 'r') as file:
        ip_list = json.load(file)
        if random_number == -1:
            random_number = random.randint(0, len(ip_list) - 1)
        ip_info = ip_list[random_number]
        ip_url_next = '://' + ip_info['address'] + ':' + ip_info['port']
        proxies = {'http': 'http' + ip_url_next, 'https': 'https' + ip_url_next}
        return random_number, proxies


if __name__ == '__main__':
    pass
