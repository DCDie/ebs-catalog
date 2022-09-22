from io import BytesIO
from tempfile import TemporaryFile
from unicodedata import category

from django.core.files import File
from django.test import TestCase

# Create your tests here.
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT

from apps.products.models import Attachment, Brand, Product, Category, Shop, User, Comment, ShopCategory, ShopProduct


class TaskApiTestCAse(TestCase):

    def test_get_attachments_list(self):
        response = self.client.get('/attachments/')
        self.assertEqual(HTTP_200_OK, response.status_code)
    #
    # def test_retrieve_attachments(self):
    #     attachment = Attachment.objects.create(
    #         title='Test',
    #         file_url=File(open("apps\enter\enter_categories.json", 'rb'))
    #     )
    #     response = self.client.get(f'/attachments/{attachment.id}/')
    #     self.assertEqual(HTTP_200_OK, response.status_code)

    # def test_attachment_update(self):
    #     attachment = Attachment.objects.create(title='Test',
    #                                            file_url=File(open("apps\products\\fixtures\categories.json", 'rb')))
    #     data = {
    #         'title': "gsfgfdg",
    #     }
    #     response = self.client.patch(f'/attachments/{attachment.id}/', data=data)
    #     self.assertEqual(HTTP_200_OK, response.status_code)
    ##################### BRANDS #####################################################
    def test_get_brands_list(self):
        response = self.client.get('/brands/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_retrieve_brands(self):
        brand = Brand.objects.create(title='Test', languages='Test')
        response = self.client.get(f'/brands/{brand.id}/')
        self.assertEqual(HTTP_200_OK, response.status_code)


    def test_create_brands(self):
        data = {
            "title": "tryrghty",
        }
        response = self.client.post(f'/brands/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_update_brands(self):
        brand = Brand.objects.create(title='Test', languages='Test')
        data = {
            "title": "tryrty",
        }
        response = self.client.put(f'/brands/{brand.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_delete_brands(self):
        brand = Brand.objects.create(title='Test')
        response = self.client.delete(f'/brands/{brand.id}/')
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_partical_update_brands(self):
        brand = Brand.objects.create(title='Test', languages='Test')
        data = {
            "title": "hdhhdh",
        }
        response = self.client.patch(f'/brands/{brand.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    ####################################### CATEGORY ######################
    def test_get_category_list(self):
        response = self.client.get('/categories/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_get_category_create(self):
        data = {

            "title": "afsff",

        }
        response = self.client.post('/categories/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_retrieve_category(self):
        category = Category.objects.create(title='Test', languages='Test')
        response = self.client.get(f'/categories/{category.id}/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_update_category(self):
        category = Category.objects.create(title='Test', languages='Test')
        data = {
            "title": "tryrty",

        }
        response = self.client.put(f'/categories/{category.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_partical_update_category(self):
        category = Category.objects.create(title='Test', languages='Test')
        data = {
            "title": "tryrty",

        }
        response = self.client.patch(f'/categories/{category.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_delete_category(self):
        category = Category.objects.create(title='Test', languages='Test')
        response = self.client.delete(f'/categories/{category.id}/')
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)

    ##########################PRODUCTS################################

    def test_get_products_list(self):
        response = self.client.get('/products/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_products_retriew(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test', category=category, description='Test', price=10, rating=0,
                                         verified=True)
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_products_products(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test', category=category, description='Test', price=10, rating=0,
                                         verified='True',
                                         specification='Test', languages='Test')
        data = {
            'title': 'sdfsdg',
            "description": "dgfgfddddd",
            "price": 10,
            "rating": 5,
            "verified": True,
            "category": category.id,

        }
        response = self.client.put(f'/products/{product.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_create_products(self):
        category = Category.objects.create(title='Test')
        data = {
            "title": "tryrghty",
            "description": "dgfgfddddd",
            "price": 10,
            "rating": 5,
            "verified": True,
            "category": category.id,
        }
        response = self.client.post(f'/products/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_products_partical_updates(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test', category=category, description='Test', price=10, rating=0,
                                         verified='True',
                                         specification='Test', languages='Test')
        data = {
            'title': 'sdfsdg',
            "description": "dgfgfddddd",
            "price": 10,
            "rating": 5,
            "verified": True,
            "category": category.id,

        }
        response = self.client.patch(f'/products/{product.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_delete_product(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test', category=category, description='Test', price=10, rating=0,
                                         verified='True',
                                         specification='Test', languages='Test')
        response = self.client.delete(f'/products/{product.id}/')
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)

    ##################COMMENTS#############################

    def test_get_comment_list(self):
        response = self.client.get('/comments/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_get_comment_create(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test', category=category, description='Test', price=10, rating=0,
                                         verified='True',
                                         specification='Test', languages='Test')
        shop = Shop.objects.create(title='Test', description='Test')

        data = {

            "text": "afsff",
            "rating": 5,
            'product': product.id,
            'shop': shop.id,

        }
        response = self.client.post('/comments/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_comments_retriew(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test', category=category, description='Test', price=10, rating=0,
                                         verified='True',
                                         specification='Test', languages='Test')
        shop = Shop.objects.create(title='Test', description='Test')
        comment = Comment.objects.create(text='Title', rating=0, product=product, shop=shop)
        response = self.client.get(f'/comments/{comment.id}/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_comments_update(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test', category=category, description='Test', price=10, rating=0,
                                         verified='True',
                                         specification='Test', languages='Test')
        shop = Shop.objects.create(title='Test', description='Test')
        comment = Comment.objects.create(text='Title', rating=0, product=product, shop=shop)
        data = {
            "text": "afsff",
            "rating": 5,
            'product': product.id,
            'shop': shop.id,

        }
        response = self.client.put(f'/comments/{comment.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_comments_patrical_update(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test', category=category, description='Test', price=10, rating=0,
                                         verified='True',
                                         specification='Test', languages='Test')
        shop = Shop.objects.create(title='Test', description='Test')
        comment = Comment.objects.create(text='Title', rating=0, product=product, shop=shop)
        data = {
            "text": "afsff",
            "rating": 5,
            'product': product.id,
            'shop': shop.id,

        }
        response = self.client.patch(f'/comments/{comment.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_comments_delete(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test', category=category, description='Test', price=10, rating=0,
                                         verified='True',
                                         specification='Test', languages='Test')
        shop = Shop.objects.create(title='Test', description='Test')
        comment = Comment.objects.create(text='Title', rating=0, product=product, shop=shop)
        response = self.client.delete(f'/comments/{comment.id}/', content_type='application/json')
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)

    ##################################SHOP#########################
    def test_shop_list(self):
        response = self.client.get('/shops/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_shop_create(self):
        data = {
            "title": "string",
            "description": "string",

        }
        response = self.client.post('/shops/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_shop_retriew(self):
        shop = Shop.objects.create(title='Test', description='Test')
        response = self.client.get(f'/shops/{shop.id}/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_shop_update(self):
        shop = Shop.objects.create(title='Test', description='Test')
        data = {
            "title": "string",
            "description": "string",
        }
        response = self.client.put(f'/shops/{shop.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_shop__upddate(self):
        shop = Shop.objects.create(title='Test', description='Test')
        data = {
            "title": "string",
            "description": "string",
        }
        response = self.client.patch(f'/shops/{shop.id}/', content_type='application/json', data=data)
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_shop_delete(self):
        shop = Shop.objects.create(title='Test', description='Test')

        response = self.client.delete(f'/shops/{shop.id}/', content_type='application/json')
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)

    ##########################SHOP_PRODUCTS##############################
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
        shop_category = ShopCategory.objects.create(name='name',
                                                    shop=shop)
        # f = open("media\enter\enter_categories.json", 'rb')
        # file = BytesIO(f.read())
        attachment = Attachment.objects.create(title='Test', extension='.pdf',
                                               file_url=File(open("media\enter\enter_categories.json", 'rb')))
        data = {
            "title": "string",
            "price": 4,
            "available": True,
            "shop": shop.id,
            "product": product.id,
            "shop_category": shop_category.id,
            "attachment": [attachment.id],

        }
        response = self.client.post('/shop_products/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, 201)

    def test_shop_products_retriew(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test',
                                         category=category,
                                         description='Test',
                                         price=10,
                                         rating=0,
                                         verified=True,
                                         )
        shop = Shop.objects.create(title='Test')
        shop_category = ShopCategory.objects.create(name='name',
                                                    shop=shop)
        # f = open("media\enter\enter_categories.json", 'rb')
        # file = BytesIO(f.read())
        attachment = Attachment.objects.create(title='Test', extension='.pdf',
                                               file_url=File(open("media\enter\enter_categories.json", 'rb')))
        shop_product = ShopProduct.objects.create(title='Test', price=7, available=True,
                                                  shop=shop, shop_category=shop_category)
        data = {
            "title": "string",
            "price": 4,
            "available": True,
            "shop": shop.id,
            "product": product.id,
            "shop_category": shop_category.id,
            "attachment": [attachment.id],

        }

        response = self.client.put(f'/shop_products/{shop_product.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_shop_products_patch(self):
        category = Category.objects.create(title='Test')
        product = Product.objects.create(title='Test',
                                         category=category,
                                         description='Test',
                                         price=10,
                                         rating=0,
                                         verified=True,
                                         )
        shop = Shop.objects.create(title='Test')
        shop_category = ShopCategory.objects.create(name='name',
                                                    shop=shop)
        # f = open("media\enter\enter_categories.json", 'rb')
        # file = BytesIO(f.read())
        attachment = Attachment.objects.create(title='Test', extension='.pdf',
                                               file_url=File(open("media\enter\enter_categories.json", 'rb')))
        shop_product = ShopProduct.objects.create(title='Test', price=7, available=True,
                                                  shop=shop, shop_category=shop_category)
        data = {
            "title": "string",
            "price": 4,
            "available": True,
            "shop": shop.id,
            "product": product.id,
            "shop_category": shop_category.id,
            "attachment": [attachment.id],

        }

        response = self.client.patch(f'/shop_products/{shop_product.id}/', content_type='application/json', data=data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_shop_products_delete(self):
        shop = Shop.objects.create(title='Test')
        shop_category = ShopCategory.objects.create(name='name',
                                                    shop=shop)
        shop_product = ShopProduct.objects.create(title='Test', price=7, available=True,
                                                  shop=shop, shop_category=shop_category)

        response = self.client.delete(f'/shop_products/{shop_product.id}/', content_type='application/json')
        self.assertEqual(HTTP_204_NO_CONTENT, response.status_code)
