import requests
from bs4 import BeautifulSoup

from Good import Good

if __name__ == '__main__':
    keywords = ['包','红色']

    para = '+'.join(keywords)
    url = 'https://www.amazon.cn/s/?field-keywords={}'.format(para)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    goods = []
    for item in soup.find_all('div', class_='s-item-container')[0:5]:
        img = item.find('img').get('src')
        desc = item.find('h2').get_text()
        price = item.find('span', class_='s-price').get_text()
        good = Good(desc, img, price)
        goods.append(good.tojson())

    print(goods)