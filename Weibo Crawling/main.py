#coding: utf-8
import threading

from WeiboSpider import WeiboSpider
from nameToUid import nameToUid

if __name__ == '__main__':
    file = open('cookie.txt')
    cookies_str = file.readline()
    cookies = dict()
    for line in cookies_str.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

    # parameter passed in
    nickname = '上海交通大学'
    uid = nameToUid(cookies).transfer(nickname)
    file = open(nickname + '.txt', 'w', encoding='utf-8')
    if uid == '':
        pass
    else:
        threads = []
        lock = threading.Lock()
        for i in range(20):
            page = str(i + 1)
            spider = WeiboSpider(lock, cookies, uid, page, file)
            spider.start()
            threads.append(spider)
        for t in threads:
            t.join()
        file.close()