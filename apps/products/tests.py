import requests
from django.core.files import File
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from apps.products.models import (
    Attachment,
    Brand,
    Product,
    Category,
    Shop,
    Comment,
    ShopCategory,
    ShopProduct
)

fake = Faker()


class BrandTestCase(APITestCase):

    def test_get_attachments_list(self):
        response = self.client.get(
            '/attachments/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_brands_list(self):
        response = self.client.get(
            '/brands/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_brands(self):
        brand = Brand.objects.create(
            title=fake.sentence()
        )
        response = self.client.get(
            f'/brands/{brand.id}/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_create_brands(self):
        data = {
            'title': fake.sentence()
        }
        response = self.client.post(
            '/brands/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_update_brands(self):
        brand = Brand.objects.create(
            title=fake.sentence()
        )
        data = {
            "title": fake.sentence(),
        }
        response = self.client.put(
            f'/brands/{brand.id}/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_brands(self):
        brand = Brand.objects.create(
            title=fake.sentence()
        )
        response = self.client.delete(
            f'/brands/{brand.id}/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_partial_update_brands(self):
        brand = Brand.objects.create(
            title=fake.sentence()
        )
        data = {
            "title": fake.sentence()
        }
        response = self.client.patch(
            f'/brands/{brand.id}/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class CategoryTestCase(APITestCase):

    def test_get_category_list(self):
        response = self.client.get(
            '/categories/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_category_create(self):
        data = {
            "title": fake.sentence()
        }
        response = self.client.post(
            '/categories/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_retrieve_category(self):
        category = Category.objects.create(
            title=fake.sentence()
        )
        response = self.client.get(
            f'/categories/{category.id}/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_category(self):
        category = Category.objects.create(
            title=fake.sentence()
        )
        data = {
            "title": fake.sentence()
        }
        response = self.client.put(
            f'/categories/{category.id}/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_partial_update_category(self):
        category = Category.objects.create(
            title=fake.sentence()
        )
        data = {
            "title": fake.sentence()
        }
        response = self.client.patch(
            f'/categories/{category.id}/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_category(self):
        category = Category.objects.create(title=fake.sentence())
        response = self.client.delete(f'/categories/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ProductTestCase(APITestCase):

    def test_get_products_list(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_products_retrieve(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=10,
            rating=0,
            verified=True
        )
        product.category.add(category)
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_products_products(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=8,
            rating=2,
            verified='True',
            specification='Test', languages='Test'
        )
        product.category.add(category)
        data = {
            'title': fake.sentence(),
            "description": fake.sentence(),
            "price": fake.random_number(),
            "rating": 5,
            "verified": True,
            "category": [category.id],
        }
        response = self.client.put(f'/products/{product.id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_products(self):
        category = Category.objects.create(title='Test')
        data = {
            "title": fake.sentence(),
            "description": fake.sentence(),
            "price": 10,
            "rating": 5,
            "verified": True,
            "category": [category.id],
        }
        response = self.client.post('/products/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_products_partial_update(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=10,
            rating=0,
            verified='True',
            specification='Test',
        )
        product.category.add(category)
        data = {
            'title': fake.sentence(),
            "description": fake.sentence(),
            "price": fake.random_number(),
            "rating": 5,
            "verified": True,
            "category": [category.id],
        }
        response = self.client.patch(f'/products/{product.id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description='Test',
            price=10,
            rating=0,
            verified='True',
            specification='Test',
        )
        product.category.add(category)
        response = self.client.delete(f'/products/{product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CommentTestCase(APITestCase):

    def test_get_comment_list(self):
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_comment_create(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=10,
            rating=0,
            verified='True',
            specification='Test',
        )
        product.category.add(category)
        shop = Shop.objects.create(
            title=fake.sentence(),
            description=fake.sentence()
        )

        data = {
            "text": fake.sentence(),
            "rating": 5,
            'product': product.id,
            'shop': shop.id,
        }
        response = self.client.post('/comments/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comments_retrieve(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=10,
            rating=0,
            verified='True',
            specification='Test',
            languages='Test'
        )
        product.category.add(category)
        shop = Shop.objects.create(
            title=fake.sentence(),
            description=fake.sentence()
        )
        comment = Comment.objects.create(
            text=fake.sentence(),
            rating=0,
            product=product,
            shop=shop
        )
        response = self.client.get(f'/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comments_update(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=10,
            rating=0,
            verified='True',
            specification='Test'
        )
        product.category.add(category)
        shop = Shop.objects.create(
            title=fake.sentence(),
            description=fake.sentence()
        )
        comment = Comment.objects.create(
            text=fake.sentence(),
            rating=0,
            product=product,
            shop=shop
        )
        data = {
            "text": fake.sentence(),
            "rating": 5,
            'product': product.id,
            'shop': shop.id,
        }
        response = self.client.put(f'/comments/{comment.id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comments_partial_update(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=10,
            rating=0,
            verified='True',
            specification='Test'
        )
        product.category.add(category)
        shop = Shop.objects.create(
            title=fake.sentence(),
            description=fake.sentence())
        comment = Comment.objects.create(
            text=fake.sentence(),
            rating=0,
            product=product,
            shop=shop
        )
        data = {
            "text": fake.sentence(),
            "rating": 5,
            'product': product.id,
            'shop': shop.id,
        }
        response = self.client.patch(f'/comments/{comment.id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comments_delete(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=10,
            rating=0,
            verified='True',
            specification='Test',
        )
        product.category.add(category)
        shop = Shop.objects.create(
            title=fake.sentence(),
            description=fake.sentence()
        )
        comment = Comment.objects.create(
            text=fake.sentence(),
            rating=0,
            product=product,
            shop=shop
        )
        response = self.client.delete(f'/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ShopTestCase(APITestCase):

    def test_shop_list(self):
        response = self.client.get('/shops/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_create(self):
        data = {
            "title": fake.sentence(),
            "description": fake.sentence(),
        }
        response = self.client.post('/shops/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_shop_retrieve(self):
        shop = Shop.objects.create(
            title=fake.sentence(),
            description=fake.sentence()
        )
        response = self.client.get(f'/shops/{shop.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_update(self):
        shop = Shop.objects.create(
            title=fake.sentence(),
            description=fake.sentence()
        )
        data = {
            "title": fake.sentence(),
            "description": fake.sentence(),
        }
        response = self.client.put(f'/shops/{shop.id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop__update(self):
        shop = Shop.objects.create(
            title=fake.sentence(),
            description=fake.sentence()
        )
        data = {
            "title": fake.sentence(),
            "description": fake.sentence(),
        }
        response = self.client.patch(f'/shops/{shop.id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_delete(self):
        shop = Shop.objects.create(
            title=fake.sentence(),
            description=fake.sentence()
        )

        response = self.client.delete(f'/shops/{shop.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ShopProductTestCase(APITestCase):
    def setUp(self) -> None:
        url = 'https://www.orimi.com/pdf-test.pdf'
        response = requests.get(url)
        open(
            file=r'apps\products\fixtures\test.pdf',
            mode='wb'
        ).write(
            response.content
        )

    def test_shop_products_list(self):
        response = self.client.get('/shop_products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_products_create(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=10,
            rating=0,
            verified=True,
        )
        product.category.add(category)
        shop = Shop.objects.create(title=fake.sentence())
        shop_category = ShopCategory.objects.create(
            name=fake.sentence(),
            shop=shop
        )

        attachment = Attachment.objects.create(
            title='Test',
            extension='.pdf',
            file_url=File(open(r"apps\products\fixtures\test.pdf", mode='rb'))
        )
        data = {
            "title": fake.sentence(),
            "price": 7,
            "available": True,
            "shop": shop.id,
            "product": product.id,
            "category": [category.id],
            "shop_category": shop_category.id,
            "attachments": [attachment.id],
        }
        response = self.client.post('/shop_products/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_shop_products_retrieve(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=10,
            rating=0,
            verified=True,
        )
        product.category.add(category)
        shop = Shop.objects.create(title=fake.sentence())
        shop_category = ShopCategory.objects.create(name=fake.sentence(),
                                                    shop=shop)

        attachment = Attachment.objects.create(
            title=fake.sentence(),
            extension='.pdf',
            file_url=File(open(r"apps\products\fixtures\test.pdf", mode='rb'))
        )
        shop_product = ShopProduct.objects.create(
            title=fake.sentence(),
            price=7,
            available=True,
            shop=shop,
            shop_category=shop_category
        )
        data = {
            "title": fake.sentence(),
            "price": 10,
            "available": True,
            "shop": shop.id,
            "product": product.id,
            "category": [category.id],
            "shop_category": shop_category.id,
            "attachments": [attachment.id],
        }

        response = self.client.put(f'/shop_products/{shop_product.pk}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_products_patch(self):
        category = Category.objects.create(title=fake.sentence())
        product = Product.objects.create(
            title=fake.sentence(),
            description=fake.sentence(),
            price=10,
            rating=0,
            verified=True,
        )
        product.category.add(category)
        shop = Shop.objects.create(title=fake.sentence())
        shop_category = ShopCategory.objects.create(
            name=fake.sentence(),
            shop=shop
        )

        attachment = Attachment.objects.create(
            title=fake.sentence(),
            extension='.pdf',
            file_url=File(open(r"apps\products\fixtures\test.pdf", mode='rb'))
        )
        shop_product = ShopProduct.objects.create(
            title=fake.sentence(),
            price=7,
            available=True,
            shop=shop,
            shop_category=shop_category
        )
        data = {
            "title": fake.sentence(),
            "price": 23,
            "available": True,
            "shop": shop.id,
            "product": product.id,
            "shop_category": shop_category.id,
            "attachments": [attachment.id],
        }

        response = self.client.patch(f'/shop_products/{shop_product.pk}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shop_products_delete(self):
        shop = Shop.objects.create(title=fake.sentence())
        shop_category = ShopCategory.objects.create(
            name=fake.sentence(),
            shop=shop
        )
        shop_product = ShopProduct.objects.create(
            title=fake.sentence(),
            price=7,
            available=True,
            shop=shop,
            shop_category=shop_category
        )

        response = self.client.delete(f'/shop_products/{shop_product.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
