from pathlib import Path
from faker import Faker

import requests
from django.core.files import File
from django.test import TestCase
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT

from apps.products.models import Attachment, \
    Brand, \
    Product, \
    Category, \
    Shop, \
    Comment, \
    ShopCategory, \
    ShopProduct

fake = Faker()


class TaskApiTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        URL = "https://www.orimi.com/pdf-test.pdf"
        response = requests.get(URL)
        open(Path("apps\\products\\fixtures\\test.pdf").as_posix(), "wb").write(response.content)

    def test_get_attachments_list(self):
        response = self.client.get('/attachments/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_get_brands_list(self):
        response = self.client.get('/brands/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_retrieve_brands(self):
        brand = Brand.objects.create(title='Test', languages='Test')
        response = self.client.get(f'/brands/{brand.id}/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_create_brands(self):
        data = {
            'title': fake.sentence()
        }
        response = self.client.post('/brands/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_update_brands(self):
        brand = Brand.objects.create(title=fake.sentence())
        data = {
            "title": fake.sentence(),
        }
        response = self.client.put(f'/brands/{brand.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_delete_brands(self):
        brand = Brand.objects.create(title='Test')
        response = self.client.delete(f'/brands/{brand.id}/')
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_partical_update_brands(self):
        brand = Brand.objects.create(title=fake.sentence())
        data = {
            "title": fake.sentence()
        }
        response = self.client.patch(f'/brands/{brand.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_get_category_list(self):
        response = self.client.get('/categories/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_get_category_create(self):
        data = {

            "title": fake.sentence()

        }
        response = self.client.post('/categories/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_retrieve_category(self):
        category = Category.objects.create(title=fake.sentence())
        response = self.client.get(f'/categories/{category.id}/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_update_category(self):
        category = Category.objects.create(title=fake.sentence())
        data = {
            "title": fake.sentence()

        }
        response = self.client.put(f'/categories/{category.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_partical_update_category(self):
        category = Category.objects.create(title=fake.sentence())
        data = {
            "title": fake.sentence()

        }
        response = self.client.patch(f'/categories/{category.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_delete_category(self):
        category = Category.objects.create(title=fake.sentence())
        response = self.client.delete(f'/categories/{category.id}/')
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)

    def test_get_products_list(self):
        response = self.client.get('/products/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_products_retriew(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test',
                                         category=category,
                                         description='Test',
                                         price=10,
                                         rating=0,
                                         verified=True)
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_products_products(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title=fake.sentence(),
                                         category=category,
                                         description=fake.sentence(),
                                         price=8,
                                         rating=2,
                                         verified='True',
                                         specification='Test', languages='Test')
        data = {
            'title': fake.sentence(),
            "description": fake.sentence(),
            "price": fake.random_number(),
            "rating": 5,
            "verified": True,
            "category": category.id,

        }
        response = self.client.put(f'/products/{product.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_create_products(self):
        category = Category.objects.create(title='Test')
        data = {
            "title": fake.sentence(),
            "description": fake.sentence(),
            "price": 10,
            "rating": 5,
            "verified": True,
            "category": category.id,
        }
        response = self.client.post('/products/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_products_partial_update(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(title=fake.sentence(),
                                         category=category,
                                         description=fake.sentence(),
                                         price=10,
                                         rating=0,
                                         verified='True',
                                         specification='Test',
                                       )
        data = {
            'title': fake.sentence(),
            "description": fake.sentence(),
            "price": fake.random_number(),
            "rating": 5,
            "verified": True,
            "category": category.id,

        }
        response = self.client.patch(f'/products/{product.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_delete_product(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(title=fake.sentence(),
                                         category=category,
                                         description='Test',
                                         price=10,
                                         rating=0,
                                         verified='True',
                                         specification='Test',
                                         )
        response = self.client.delete(f'/products/{product.id}/')
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)

    def test_get_comment_list(self):
        response = self.client.get('/comments/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_get_comment_create(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(title=fake.sentence(),
                                         category=category,
                                         description=fake.sentence(),
                                         price=10,
                                         rating=0,
                                         verified='True',
                                         specification='Test',
                                         )
        shop = Shop.objects.create(title='Test', description='Test')

        data = {

            "text": fake.sentence(),
            "rating": 5,
            'product': product.id,
            'shop': shop.id,

        }
        response = self.client.post('/comments/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_comments_retriew(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(title=fake.sentence(),
                                         category=category,
                                         description=fake.sentence(),
                                         price=10,
                                         rating=0,
                                         verified='True',
                                         specification='Test',
                                         languages='Test')
        shop = Shop.objects.create(title=fake.sentence(), description=fake.sentence())
        comment = Comment.objects.create(text='Title', rating=0, product=product, shop=shop)
        response = self.client.get(f'/comments/{comment.id}/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_comments_update(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(title=fake.sentence(),
                                         category=category,
                                         description=fake.sentence(),
                                         price=10,
                                         rating=0,
                                         verified='True',
                                         specification='Test')
        shop = Shop.objects.create(title=fake.sentence(), description=fake.sentence())
        comment = Comment.objects.create(text='Title', rating=0, product=product, shop=shop)
        data = {
            "text": fake.sentence(),
            "rating": 5,
            'product': product.id,
            'shop': shop.id,

        }
        response = self.client.put(f'/comments/{comment.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_comments_patrical_update(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(title=fake.sentence(),
                                         category=category,
                                         description=fake.sentence(),
                                         price=10,
                                         rating=0,
                                         verified='True',
                                         specification='Test'
                                         )
        shop = Shop.objects.create(title='Test', description='Test')
        comment = Comment.objects.create(text='Title', rating=0, product=product, shop=shop)
        data = {
            "text": fake.sentence(),
            "rating": 5,
            'product': product.id,
            'shop': shop.id,

        }
        response = self.client.patch(f'/comments/{comment.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_comments_delete(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(title=fake.sentence(),
                                         category=category,
                                         description=fake.sentence(),
                                         price=10,
                                         rating=0,
                                         verified='True',
                                         specification='Test',

                                         )
        shop = Shop.objects.create(title=fake.sentence(), description=fake.sentence())
        comment = Comment.objects.create(text=fake.sentence(), rating=0, product=product, shop=shop)
        response = self.client.delete(f'/comments/{comment.id}/', content_type='application/json')
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)

    def test_shop_list(self):
        response = self.client.get('/shops/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_shop_create(self):
        data = {
            "title": fake.sentence(),
            "description": fake.sentence(),

        }
        response = self.client.post('/shops/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_shop_retriew(self):
        shop = Shop.objects.create(title=fake.sentence(), description=fake.sentence())
        response = self.client.get(f'/shops/{shop.id}/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_shop_update(self):
        shop = Shop.objects.create(title=fake.sentence(), description=fake.sentence())
        data = {
            "title": fake.sentence(),
            "description": fake.sentence(),
        }
        response = self.client.put(f'/shops/{shop.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_shop__upddate(self):
        shop = Shop.objects.create(title=fake.sentence(), description=fake.sentence())
        data = {
            "title": fake.sentence(),
            "description": fake.sentence(),
        }
        response = self.client.patch(f'/shops/{shop.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_shop_delete(self):
        shop = Shop.objects.create(title=fake.sentence(), description=fake.sentence())

        response = self.client.delete(f'/shops/{shop.id}/', content_type='application/json')
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)

    def test_shop_products_list(self):
        response = self.client.get('/shop_products/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_shop_products_create(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test',
                                         category=category,
                                         description='Test',
                                         price=10,
                                         rating=0,
                                         verified=True,
                                         )
        shop = Shop.objects.create(title='Test')
        shop_category = ShopCategory.objects.create(name='Test',
                                                    shop=shop)

        attachment = Attachment.objects.create(
            title='Test',
            extension='.pdf',
            file_url=File(open(Path("apps\\products\\fixtures\\test.pdf").as_posix(), 'rb'))
        )
        data = {
            "title": 'test',
            "price":7,
            "available": True,
            "shop": shop.id,
            "product": product.id,
            "shop_category": shop_category.id,
            "attachment": [attachment.id],

        }
        response = self.client.post('/shop_products/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_shop_products_retriew(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(title=fake.sentence(),
                                         category=category,
                                         description=fake.sentence(),
                                         price=10,
                                         rating=0,
                                         verified=True,
                                         )
        shop = Shop.objects.create(title=fake.sentence())
        shop_category = ShopCategory.objects.create(name=fake.sentence(),
                                                    shop=shop)

        attachment = Attachment.objects.create(
            title=fake.sentence(),
            extension='.pdf',
            file_url=File(open((Path("apps\\products\\fixtures\\test.pdf")).as_posix(), 'rb'))
        )
        shop_product = ShopProduct.objects.create(title=fake.sentence(), price=7, available=True,
                                                  shop=shop, shop_category=shop_category)
        data = {
            "title": fake.sentence(),
            "price": 10,
            "available": True,
            "shop": shop.id,
            "product": product.id,
            "shop_category": shop_category.id,
            "attachment": [attachment.id],

        }

        response = self.client.put(f'/shop_products/{shop_product.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_shop_products_patch(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(title=fake.sentence(),
                                         category=category,
                                         description=fake.sentence(),
                                         price=10,
                                         rating=0,
                                         verified=True,
                                         )
        shop = Shop.objects.create(title=fake.sentence())
        shop_category = ShopCategory.objects.create(name=fake.sentence(),
                                                    shop=shop)

        attachment = Attachment.objects.create(
            title=fake.sentence(),
            extension='.pdf',
            file_url=File(open(Path("apps\\products\\fixtures\\test.pdf").as_posix(), 'rb'))
        )
        shop_product = ShopProduct.objects.create(title=fake.sentence(), price=7, available=True,
                                                  shop=shop, shop_category=shop_category)
        data = {
            "title": fake.sentence(),
            "price": fake.random_number(),
            "available": True,
            "shop": shop.id,
            "product": product.id,
            "shop_category": shop_category.id,
            "attachment": [attachment.id],

        }

        response = self.client.patch(f'/shop_products/{shop_product.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_shop_products_delete(self):
        shop = Shop.objects.create(title=fake.sentence())
        shop_category = ShopCategory.objects.create(name=fake.sentence(),
                                                    shop=shop)
        shop_product = ShopProduct.objects.create(title=fake.sentence(),
                                                  price=7,
                                                  available=True,
                                                  shop=shop,
                                                  shop_category=shop_category)

        response = self.client.delete(f'/shop_products/{shop_product.id}/', content_type='application/json')
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)
