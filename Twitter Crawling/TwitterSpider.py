import threading

import requests
from bs4 import BeautifulSoup


class TwitterSpider(threading.Thread):
    def __init__(self, username, begin_date, end_date, file, lock):
        threading.Thread.__init__(self)
        self.begin_date = begin_date
        self.end_date = end_date
        self.name = username
        self.file = file
        self.lock = lock

    def run(self):
        url = 'https://mobile.twitter.com/search?l=&q=from%3A' + self.name + '%20since%3A' \
              + self.begin_date + '%20until%3A' + self.end_date + '&src=typd'
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        tweets = []
        for tweet in soup.find_all('div', class_='dir-ltr'):
            tweets.append(tweet.get_text())

        with self.lock:
            for tweet in tweets:
                self.file.write(tweet)
