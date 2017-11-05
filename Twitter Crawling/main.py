import datetime
import threading

from TwitterSpider import TwitterSpider

if __name__ == '__main__':
    username = 'sleeplesstyphon‏'

    today = datetime.date.today()
    duration = datetime.timedelta(days=7)
    dates = []
    i = 0
    while i != 12:
        today = today - duration
        dates.append(today)
        i += 1
    threads = []
    file = open(username + '.txt', 'w', encoding='utf-8')
    lock = threading.Lock()
    for date in dates:
        begin_date = str(date)
        end_date = str(date + datetime.timedelta(days=6))
        spider = TwitterSpider(username, begin_date, end_date, file, lock)
        spider.start()
        threads.append(spider)

    for t in threads:
        t.join()
    file.close()
