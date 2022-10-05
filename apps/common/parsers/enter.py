import json
import pathlib
import time
from typing import Optional

import requests
from bs4 import BeautifulSoup
from django.template.defaultfilters import slugify
from fake_useragent import UserAgent
from django.conf import settings


class EnterParser:
    user = UserAgent()
    agent = user.random

    headers = {
        'User-Agent': agent,
    }

    def __init__(self) -> None:
        self.table_goods = []
        self.category_name = str
        self.path = settings.ENTER_ROOT
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def logging(
            message: str,
            data: Optional[str] = None,
            execution_time: Optional[float] = None
    ) -> None:
        print(f"{message} | Data: {data} | Time: {execution_time} sec.")

    def get_categories(self) -> None:
        start = time.process_time()
        url = 'https://enter.online/'

        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        categories = soup.select('.first-level > .first-level')
        categories_data = {}
        for category in categories:
            category_name = category.select('a')[0].text.replace('\n', '')
            subcategories = category.select(
                '.uk-position-top-left > .uk-nav.tm-mobile-menu-nav > .blue'
            )
            categories_data[category_name] = {}
            for subcategory in subcategories:
                subcategory_link = subcategory.get('href')

                # If category exists write
                if subcategory_link:
                    categories_data[category_name][subcategory.text] = subcategory_link
        with open(
                f'{self.path}/enter_categories.json', 'w+', encoding='utf-8'
        ) as read_file:
            read_file.write(json.dumps(categories_data, ensure_ascii=False))
            self.logging(
                message='File: enter_categories.json - saved',
                execution_time=time.process_time() - start,
            )

    def get_products(self) -> None:
        with open(f"{self.path}/enter_categories.json", "rb") as read_file:
            shop_title = 'enter'
            categories = json.load(read_file)
        for category, category_data in categories.items():

            for subcategory in category_data:
                data = {}
                data[subcategory] = []
                page = 1
                while True:
                    # Start timer
                    start = time.process_time()
                    link = category_data[subcategory]

                    # Request method to goods
                    response = requests.get(
                        f'{link}?page={page}',
                        headers=self.headers,
                        allow_redirects=False,
                    )

                    soup = BeautifulSoup(response.text, 'html.parser')
                    goods = soup.select('.product-card > div > .grid-item')

                    if not bool(goods):
                        break
                        # Get goods values
                    for good in goods:
                        # noinspection PyUnusedLocal
                        price = 0
                        if price := good.select_one(
                                '.grid-price-cart > .grid-price > .price'
                        ):
                            price = price.text
                        elif discount_price := good.select_one(
                                '.grid-price-cart > .grid-price > .price-new'
                        ):
                            price = discount_price.text
                        title = good.select_one('div > a > .product-title').text
                        description = good.select_one('div > a > .product-descr').text
                        label = slugify(f'{shop_title}, {title}, {description}, {price}')

                        # Save goods data in dict
                        dictionary = {
                            'label': label,
                            'title': title,
                            'description': description,
                            'price': price,
                            'available': bool(good.attrs.get('data-stock'))
                        }
                        data[subcategory].append(dictionary)
                    self.logging(
                        message=f'Added {subcategory}',
                        data=f'Status code: {response.status_code} | Page: {page} | URL: {response.url}',
                        execution_time=time.process_time() - start
                    )
                    page += 1

                    # with open(
                    #         f'{self.path}/enter_items_{category}.json',
                    #         'w+',
                    #         encoding='utf-8'
                    # ) as fp:
                    #     fp.write(json.dumps(data, indent=5, ensure_ascii=False))
