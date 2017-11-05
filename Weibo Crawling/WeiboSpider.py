import threading

import requests
from bs4 import BeautifulSoup


class WeiboSpider(threading.Thread):
    def __init__(self, lock, cookies, id, page, file):
        threading.Thread.__init__(self)
        self.id = id
        self.page = page
        self.cookies = cookies
        self.file = file
        self.lock = lock

    def run(self):
        weibo_list = []
        url = 'https://weibo.cn{}?page={}'.format(self.id, self.page)
        response = requests.get(url, cookies=self.cookies)
        soup = BeautifulSoup(response.content, 'html.parser')
        for weibo in soup.find_all('span', class_='ctt'):
            weibo_list.append(weibo.get_text())

        with self.lock:
            for weibo in weibo_list:
                self.file.write(weibo + '\n')





