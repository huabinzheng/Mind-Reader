import requests
from bs4 import BeautifulSoup


class nameToUid(object):
    def __init__(self, cookies):
        self.cookies = cookies

    def transfer(self, name):
        search_url = 'https://weibo.cn/search/user/?keyword={}'.format(name)
        response = requests.post(search_url, cookies=self.cookies)
        soup = BeautifulSoup(response.content, 'html.parser')
        url = ''
        for tr in soup.find_all('table'):
            for td in tr.find_all('a'):
                username =  td.get_text().strip()
                if username.lower() == name.lower():
                    url = td.get('href').split('?')[0]
                    break
        return url