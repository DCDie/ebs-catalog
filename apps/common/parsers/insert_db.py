import datetime
import json
import os
import time
from typing import Optional

from django.conf import settings

from apps.products.models import (
    ShopCategory,
    ShopProduct,
    Shop
)


class InsertDataBase:

    def __init__(self) -> None:
        self.directory = f'{settings.BASE_DIR}/media'

    @staticmethod
    def logging(message: str, data: Optional[str] = None, execution_time: Optional[datetime] = None) -> None:
        print(f"{message} | Data: {data} | Time: {execution_time} sec.")

    def add_shop_category(self) -> None:
        for file in os.listdir(self.directory):
            shop_name = os.fsdecode(file)
            for filename in os.listdir(f'{self.directory}/{shop_name}'):
                if 'items' in filename:
                    start = time.process_time()
                    with open(f'media/{shop_name}/{filename}', encoding='utf-8') as fp:
                        data = []
                        category_items = json.load(fp)
                    for item_name in category_items:
                        try:
                            shop_queryset = Shop.objects.get(
                                title=shop_name
                            ).id
                            data.append(
                                ShopCategory(
                                    name=item_name,
                                    shop_id=shop_queryset
                                ))
                        except Shop.DoesNotExist:
                            raise ValueError('Shop not found')
                    ShopCategory.objects.bulk_create(
                        objs=data,
                        ignore_conflicts=True
                    )
                    self.logging(
                        message='Categories added',
                        execution_time=time.process_time() - start
                    )

    def add_shop_products(self) -> None:
        for file in os.listdir(self.directory):
            shop_name = os.fsdecode(file)
            for filename in os.listdir(f'{self.directory}/{shop_name}'):
                if 'items' in filename:
                    start = time.process_time()
                    with open(f'media/{shop_name}/{filename}', encoding='utf-8') as fp:
                        category_items = json.load(fp)
                        data = []
                        for category_name, category_data_value in category_items.items():
                            for category_data in category_data_value:
                                shop_category_queryset = list(ShopCategory.objects.filter(
                                    name=category_name
                                ).values_list(
                                    'id',
                                    'category_id',
                                    'shop_id'
                                ))
                                for object_id, category_id, shop_id in shop_category_queryset:
                                    price = ''.join((category_data.get('price')).split()[:-1])
                                    data.append(
                                        ShopProduct(
                                            title=category_data.get('title'),
                                            description=category_data.get('description'),
                                            price=price,
                                            available=category_data.get('available'),
                                            shop_category_id=object_id,
                                            shop_id=shop_id,
                                            category_id=category_id
                                        )
                                    )
                        ShopProduct.objects.bulk_update_or_create(
                            objs=data,
                            update_fields=['available', 'price'],
                            match_field=['title']
                        )
                        self.logging(
                            message='New file data - added',
                            execution_time=time.process_time() - start
                        )
