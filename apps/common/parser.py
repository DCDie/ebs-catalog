import json

from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests


class Parsing:
    ua = UserAgent()
    agent = ua.random

    headers = {
        'User-Agent': agent
    }

    def __init__(self):
        self.category = {}
        self.table_goods = {}
        self.page = 1

    @staticmethod
    def logging(message, data=None):
        print(f'{message} | Data: {data}')

    def get_category_link(self):
        url = 'https://enter.online/'

        html = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        categories = soup.select('.uk-position-top-left > .uk-nav.tm-mobile-menu-nav > .blue')
        for main_category in categories:
            if main_category.get('href') is None:
                continue
            else:
                dictionary = {
                    'category_link': main_category.get('href')
                }
                self.category[main_category.text] = dictionary
        with open('good_category.json', 'w+', encoding='utf-8') as fp:
            fp.write(json.dumps(self.category))
            self.logging('File good_category.json - saved')

    def goods_details(self):
        with open("good_category.json", "rb") as read_file:
            data = json.load(read_file)

            for key, value in zip(data.keys(), data.values()):
                while True:
                    link = value['category_link']
                    html = requests.get(f'{link}?page={self.page}', headers=self.headers, allow_redirects=False)
                    soup = BeautifulSoup(html.text, 'html.parser')
                    goods = soup.select('.product-card > div > .grid-item')
                    if not goods:
                        self.page = 1
                        break
                    for good in goods:
                        html_price = good.select('.grid-price-cart > .grid-price > .price')
                        price = ''.join([price.text for price in html_price])
                        html_title = good.select('div > a > .product-title')
                        title = ''.join([i.text for i in html_title])
                        html_description = good.select('div > a > .product-descr')
                        description = ''.join([i.text for i in html_description])
                        html_link = good.select('div > a')
                        link = html_link[0].get('href')

                        dictionary = {
                            'link': link,
                            'title': title,
                            'description': description,
                            'price': price
                        }
                        self.table_goods[key] = dictionary
                    with open('grid_items.json', 'a', encoding='utf-8') as fp:
                        fp.write(json.dumps(self.table_goods))
                    self.page += 1
                    self.logging(
                        'Added good card', f'Status code: {html.status_code} | Page: {self.page - 1} | URL: {html.url}'
                    )





if __name__ == '__main__':
    parsing = Parsing()
    # parsing.get_category_link()
    parsing.goods_details()
