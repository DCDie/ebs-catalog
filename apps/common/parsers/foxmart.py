import json
import pathlib
import time
from typing import Optional

import requests
from requests.adapters import HTTPAdapter, Retry
from bs4 import BeautifulSoup
from django.conf import settings
from django.template.defaultfilters import slugify
from fake_useragent import UserAgent


# noinspection SpellCheckingInspection
class FoxmartParser:
    user = UserAgent()
    agent = user.random

    headers = {
        'User-Agent': agent,
    }

    def __init__(self) -> None:
        self.path = settings.FOXMART_ROOT
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def logging(message: str, data: Optional[str] = None, execution_time: Optional[float] = None) -> None:
        print(f"{message} | Data: {data} | Time: {execution_time} sec.")

    def get_categories(self) -> None:
        start = time.process_time()
        url = "https://www.foxmart.md/"
        response = requests.get(url=url, headers=self.headers)
        html = BeautifulSoup(response.text, 'html.parser')
        categories_data = []
        for el in html.select('.uk-parent'):
            for category in el.select('a'):
                subcategory = category.attrs
                if subcategory.get('href').split('/')[-1]:
                    obj = {
                        'title': category.text,
                        'url': subcategory.get('href'),
                        'id': subcategory.get('href').split('/')[-1],
                    }
                    categories_data.append(obj)

        with open(f"{self.path}/foxmart_categories.json", "w", encoding='utf-8') as file:
            file.write(json.dumps(categories_data, indent=4, ensure_ascii=False))
            self.logging(
                message='File:foxmart_categories.json - was saved',
                execution_time=time.process_time() - start
            )

    def get_products(self) -> None:
        with open(f"{self.path}/foxmart_categories.json", "rb") as read_file:
            shop_title = 'foxmart'
            categories = json.load(read_file)
        for subcategory in categories:
            data = {}
            subcategory_id = subcategory.get('id')
            category = subcategory.get('title')
            page = 1
            data[category] = []
            while True:
                start = time.process_time()
                url = f"https://www.foxmart.md/api/client/products/catalog?items=15&" \
                      f"page={page}&category={subcategory_id}&sort=popularity&order=desc"
                retries = Retry(
                    total=5,
                    backoff_factor=0.1,
                    status_forcelist=[429, 500, 502, 503, 504]
                )
                adapter = HTTPAdapter(max_retries=retries)
                session = requests.Session()
                session.mount("https://", adapter)
                response = session.get(url=url, headers=self.headers)

                if not response.ok:
                    break
                products_dict = json.loads(response.content.decode())
                products = products_dict.get('products')

                for product in products:
                    product_id = product.get('productId')
                    title = product.get('product')
                    description = product.get('shortDescription')
                    price = product.get('price')
                    available = product.get('inStock')
                    label = slugify(f'{shop_title} ,{title}, {description}, {price}, {product_id}')

                    dictionary = {
                        'label': label,
                        'title': title,
                        'description': description,
                        'price': price,
                        'available': available
                    }

                    data[category].append(dictionary)
                self.logging(
                    message='Added subcategory',
                    data=f'| Page: {page}',
                    execution_time=time.process_time() - start
                )
                page += 1
                with open(f'{self.path}/foxmart_items_{category}.json', 'w+', encoding='utf-8') as file:
                    file.write(json.dumps(data, indent=5, ensure_ascii=False))
