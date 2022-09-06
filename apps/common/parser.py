import json
import copy
import time
from json import JSONDecodeError

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Parsing:
    ua = UserAgent()
    agent = ua.random

    headers = {
        'User-Agent': agent,
    }

    def __init__(self):
        self.category = {}
        self.category_data = []
        self.table_goods = []
        self.page = 1
        self.category_name = str
        self.link = None
        self.dictionary_data = None
        self.dictionary_row_data = []

    @staticmethod
    def logging(message, data=None, execution_time=None):
        print(f"{message} | Data: {data} | Time: {execution_time} sec.")

    def get_category_link(self):
        start = time.process_time()
        url = 'https://enter.online/'

        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        main_categories = soup.select('.first-level > .first-level')
        for main_category in main_categories:
            main_category_name = main_category.select('a')[0].text
            subcategories = main_category.select('.uk-position-top-left > .uk-nav.tm-mobile-menu-nav > .blue')
            for subcategory in subcategories:
                subcategory_link = subcategory.get('href')

                # Check if subcategory is valid
                if not subcategory_link:
                    continue
                else:
                    dictionary = {
                        f'{subcategory.text}': {
                            'category_link': subcategory_link
                        }
                    }
                    self.dictionary_row_data.append(dictionary)
                    self.dictionary_data = copy.deepcopy(self.dictionary_row_data)

            self.category[main_category_name] = self.dictionary_data
            self.dictionary_row_data.clear()
        with open('good_category.json', 'w+', encoding='utf-8') as fp:
            fp.write(json.dumps(self.category).replace(r'\n', ''))
            self.logging(
                message='File good_category.json - saved',
                execution_time=time.process_time() - start
            )

    def goods_details(self):
        with open("good_category.json", "rb") as read_file:
            data = json.load(read_file)
            for category in data:
                main_category = category
                for subcategory in data[category]:
                    for subcategory_key, subcategory_value in subcategory.items():
                        subcategory_name = subcategory_key
                        for subcategory_link_key, subcategory_link_value in subcategory_value.items():
                            while True:
                                # Start timer
                                start = time.process_time()

                                self.link = subcategory_link_value

                                # Request method to goods
                                response = requests.get(
                                    f'{self.link}?page={self.page}',
                                    headers=self.headers,
                                    allow_redirects=False
                                )
                                # Check if request method has redirect
                                if response.is_redirect:
                                    redirected_link = response.headers['Location']
                                    self.link = redirected_link
                                    response = requests.get(
                                        f'{self.link}?page={self.page}',
                                        headers=self.headers,
                                        allow_redirects=False
                                    )
                                soup = BeautifulSoup(response.text, 'html.parser')
                                goods = soup.select('.product-card > div > .grid-item')

                                # Check if goods are valid
                                if not goods:
                                    self.page = 1
                                    break

                                # Get goods values
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

                                    # Save goods data in dict
                                    dictionary = {
                                        'link': link,
                                        'title': title,
                                        'description': description,
                                        'price': price if price else discount_price,
                                        'available': False if not_available else True
                                    }

                                    # Save goods data in new variable if category is changed
                                    if self.category_name == main_category:
                                        self.table_goods.append({subcategory_name: dictionary})
                                    else:
                                        self.table_goods.clear()
                                        self.table_goods.append({subcategory_name: dictionary})

                                # Check goods category and save it file
                                if self.category_name == main_category:
                                    # If goods json is already saved and has data
                                    try:
                                        with open(f'grid_items_{self.category_name}.json') as fp:
                                            old_table_goods = json.load(fp)
                                        old_table_goods.extend(self.table_goods)
                                        with open(f'grid_items_{self.category_name}.json', 'w+',
                                                  encoding='utf-8') as fp:
                                            fp.write(json.dumps(old_table_goods).replace(r'\n', ''))
                                    # If goods json isn't created or it's empty
                                    except (JSONDecodeError, FileNotFoundError):
                                        with open(f'grid_items_{self.category_name}.json', 'w+',
                                                  encoding='utf-8') as fp:
                                            fp.write(json.dumps(self.table_goods).replace(r'\n', ''))
                                    finally:
                                        self.category_name = main_category
                                        self.logging(
                                            message='Added goods card',
                                            data=f'Status code: {response.status_code} '
                                                 f'| Page: {self.page} | URL: {response.url}',
                                            execution_time=time.process_time() - start
                                        )
                                        self.page += 1
                                # Save goods data to new json if category is changed
                                else:
                                    with open(f'grid_items_{main_category}.json', 'w+',
                                              encoding='utf-8') as fp:
                                        fp.write(json.dumps(self.table_goods).replace(r'\n', ''))
                                        self.category_name = main_category
                                        self.logging(
                                            message='Added goods card',
                                            data=f'Status code: {response.status_code} '
                                                 f'| Page: {self.page} | URL: {response.url}',
                                            execution_time=time.process_time() - start
                                        )
                                        self.page += 1


def main():
    parsing = Parsing()
    parsing.get_category_link()
    parsing.goods_details()


if __name__ == '__main__':
    main()
