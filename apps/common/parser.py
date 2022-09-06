import json
import time
from json import JSONDecodeError

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class Parsing:
    user = UserAgent()
    agent = user.random

    headers = {
        'User-Agent': agent,
    }

    def __init__(self):
        self.table_goods = []
        self.category_name = str

    @staticmethod
    def logging(message, data=None, execution_time=None):
        print(f"{message} | Data: {data} | Time: {execution_time} sec.")

    def get_categories(self):
        start = time.process_time()
        url = 'https://enter.online/'

        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        categories = soup.select('.first-level > .first-level')
        categories_data = {}
        for category in categories:
            category_name = category.select('a')[0].text.replace('\n', '')
            subcategories = category.select('.uk-position-top-left > .uk-nav.tm-mobile-menu-nav > .blue')
            categories_data[category_name] = {}
            for subcategory in subcategories:
                subcategory_link = subcategory.get('href')

                # If category exists write
                if subcategory_link:
                    categories_data[category_name][subcategory.text] = subcategory_link
        with open('categories.json', 'w+', encoding='utf-8') as fp:
            fp.write(json.dumps(categories_data))
            self.logging(
                message='File categories.json - saved',
                execution_time=time.process_time() - start
            )

    def get_products(self):
        with open("categories.json", "rb") as read_file:
            categories = json.load(read_file)
            for category, category_data in categories.items():
                page = 1
                for subcategory in category_data:
                    # Start timer
                    start = time.process_time()

                    link = category_data[subcategory]

                    # Request method to goods
                    response = requests.get(
                        f'{link}?page={page}',
                        headers=self.headers,
                        allow_redirects=False
                    )

                    soup = BeautifulSoup(response.text, 'html.parser')
                    goods = soup.select('.product-card > div > .grid-item')

                    if goods:
                        # Get goods values
                        for good in goods:
                            price = 0
                            if price := good.select_one('.grid-price-cart > .grid-price > .price'):
                                price = price.text
                            elif discount_price := good.select_one('.grid-price-cart > .grid-price > .price-new'):
                                price = discount_price.text
                            title = good.select_one('div > a > .product-title').text
                            description = good.select_one('div > a > .product-descr').text
                            link = good.select_one('div > a').get('href')

                            # Save goods data in dict
                            dictionary = {
                                'link': link,
                                'title': title,
                                'description': description,
                                'price': price,
                                'available': bool(good.attrs.get('data-stock'))
                            }

                            # Save goods data in new variable if category is changed
                            if self.category_name == category:
                                self.table_goods.append({subcategory: dictionary})
                            else:
                                self.table_goods.clear()
                                self.table_goods.append({subcategory: dictionary})

                    # Check goods category and save it file
                    if self.category_name == category:
                        # If goods json is already saved and has data
                        try:
                            with open(f'items_{self.category_name}.json') as fp:
                                old_table_goods = json.load(fp)
                            old_table_goods.extend(self.table_goods)
                            with open(f'items_{self.category_name}.json', 'w+',
                                      encoding='utf-8') as fp:
                                fp.write(json.dumps(old_table_goods).replace(r'\n', ''))
                        # If goods json isn't created or it's empty
                        except (JSONDecodeError, FileNotFoundError):
                            with open(f'items_{self.category_name}.json', 'w+',
                                      encoding='utf-8') as fp:
                                fp.write(json.dumps(self.table_goods).replace(r'\n', ''))
                        finally:
                            self.category_name = category
                            self.logging(
                                message='Added goods card',
                                data=f'Status code: {response.status_code} '
                                     f'| Page: {page} | URL: {response.url}',
                                execution_time=time.process_time() - start
                            )
                            page += 1
                    # Save goods data to new json if category is changed
                    else:
                        with open(f'items_{category}.json', 'w+',
                                  encoding='utf-8') as fp:
                            fp.write(json.dumps(self.table_goods).replace(r'\n', ''))
                            self.category_name = category
                            self.logging(
                                message='Added goods card',
                                data=f'Status code: {response.status_code} '
                                     f'| Page: {page} | URL: {response.url}',
                                execution_time=time.process_time() - start
                            )
                            page += 1


def main():
    parsing = Parsing()
    parsing.get_categories()
    parsing.get_products()


if __name__ == '__main__':
    main()
