import json
from json import JSONDecodeError

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Parsing:
    ua = UserAgent()
    agent = ua.random

    headers = {
        'User-Agent': agent
    }

    def __init__(self):
        self.category = {}
        self.table_goods = []
        self.page = 1
        self.link = None

    @staticmethod
    def logging(message, data=None):
        print(f'{message} | Data: {data}')

    def get_category_link(self):
        url = 'https://enter.online/'

        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
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
                    self.link = value['category_link']
                    response = requests.get(
                        f'{self.link}?page={self.page}',
                        headers=self.headers,
                        allow_redirects=False
                    )

                    if response.is_redirect:
                        redirected_link = response.headers['Location']
                        self.link = redirected_link
                        response = requests.get(
                            f'{self.link}?page={self.page}',
                            headers=self.headers,
                            allow_redirects=False
                        )

                    self.logging(
                        'Added goods card',
                        f'Status code: {response.status_code} | Page: {self.page} | URL: {response.url}'
                    )
                    soup = BeautifulSoup(response.text, 'html.parser')
                    goods = soup.select('.product-card > div > .grid-item')
                    if not goods:
                        self.page = 1
                        break
                    for good in goods:
                        not_available = good.attrs.get('data-stock')
                        html_price = good.select('.grid-price-cart > .grid-price > .price')
                        html_price_discount = good.select('.grid-price-cart > .grid-price > .price-new')
                        discount_price = ''.join([price.text for price in html_price_discount])
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
                            'price': price if price else discount_price,
                            'available': False if not_available else True
                        }
                        self.table_goods.append({key: dictionary})
                    try:
                        with open('grid_items1.json') as fp:
                            old_table_goods = json.load(fp)
                        old_table_goods.extend(self.table_goods)
                        with open('grid_items1.json', 'w', encoding='utf-8') as fp:
                            fp.write(json.dumps(old_table_goods).replace(r'\n', ''))
                    except JSONDecodeError:
                        with open('grid_items1.json', 'w', encoding='utf-8') as fp:
                            fp.write(json.dumps(self.table_goods).replace(r'\n', ''))
                    finally:
                        self.page += 1


if __name__ == '__main__':
    parsing = Parsing()
    # parsing.get_category_link()
    parsing.goods_details()
