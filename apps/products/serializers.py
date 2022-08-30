from rest_framework.serializers import ModelSerializer

from apps.products.models import (
    Category,
    Comment,
    Shop,
    Attachment,
    ProductShop,
    Product
)

__all__ = [
    'CategorySerializer',
    'CommentSerializer',
    'ShopSerializer',
    'ProductSerializer',
    'AttachmentSerializer',
    'ProductShopSerializer'
]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class ProductShopSerializer(ModelSerializer):
    class Meta:
        model = ProductShop
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
