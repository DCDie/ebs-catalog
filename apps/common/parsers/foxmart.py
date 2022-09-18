import json
import pathlib
import time

import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import UserAgent
from rest_framework.status import is_success


class FoxmartParser:
    user = UserAgent()
    agent = user.random

    headers = {
        'User-Agent': agent,
    }

    def __init__(self):
        self.path = 'media/foxmart'
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def logging(message, data=None, execution_time=None):
        print(f"{message} | Data: {data} | Time: {execution_time} sec.")

    def get_categories(self) -> None:
        start = time.process_time()
        url = "https://www.foxmart.md/"
        r = requests.get(url=url, headers=self.headers)
        html = BS(r.content, 'html.parser')
        categories_data = []
        for el in html.select('.uk-parent'):
            for category in el.select('a'):
                subcategory = category.attrs
                if subcategory.get('href').split('/')[-1]:
                    obj = {
                        f'title': category.text,
                        'url': subcategory.get('href'),
                        'id': subcategory.get('href').split('/')[-1]
                    }
                    categories_data.append(obj)

        with open(f"{self.path}/foxmart_categories_.json", "w", encoding='utf-8') as file:
            file.write(json.dumps(categories_data, indent=4, ensure_ascii=False))
            self.logging(
                message='File:foxmart_categoryes_json - was saved',
                execution_time=time.process_time() - start
            )

    def get_all_products(self) -> None:
        agent = UserAgent().random
        with open(f"{self.path}/foxmart_categories_.json", "rb") as read_file:
            data = json.load(read_file)
            data_all = {}
        for subcategory in data:
            subcategory_id = subcategory.get('id')
            category = subcategory.get('title')
            page = 1
            data_all[category] = []
            while True:
                start = time.process_time()
                url = f"https://www.foxmart.md/api/client/products/catalog?items=15&page={page}&category={subcategory_id}&sort=popularity&order=desc"
                r = requests.get(url=url, headers={'User-Agent': agent})
                if not is_success(r.status_code):
                    break
                products_dict = json.loads(r.content.decode())
                products = products_dict.get('products')

                for product in products:
                    title = product.get('product')
                    shortDescription = product.get('shortDescription')
                    price = product.get('price')
                    inStock = product.get('inStock')
                    amount = product.get('amount')

                    dictionary = {
                        'title': title,
                        'Description': shortDescription,
                        'price': price,
                        'available': inStock,
                        'amount': amount

                    }

                    data_all[category].append(dictionary)
                    self.logging(
                        message=f'Added subcategory',
                        data=f'| Page: {page}',
                        execution_time=time.process_time() - start
                    )
                page += 1

                with open(f'{self.path}foxmart_items_{category}.json', 'w+', encoding='utf-8') as file:
                    file.write(json.dumps(data_all, indent=5, ensure_ascii=False))
