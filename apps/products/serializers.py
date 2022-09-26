from rest_framework.serializers import ModelSerializer

from apps.products.models import (
    Category,
    Comment,
    Shop,
    Attachment,
    ShopProduct,
    Product,
    Brand
)

__all__ = [
    'CategorySerializer',
    'CommentSerializer',
    'ShopSerializer',
    'ProductSerializer',
    'AttachmentSerializer',
    'ProductShopSerializer',
    'BrandSerializer',
]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
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
        model = ShopProduct
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BrandRetrieveSerializer(ModelSerializer):
    comment = CommentSerializer(many=True)
    category = CategorySerializer()
    atachment = AttachmentSerializer()
    product_shop = ProductShopSerializer()
    shop = ShopSerializer()
    product = ProductSerializer()

    class Meta:
        model = Brand
        fields = '__all__'


class CategoryRetrieveSerializer(ModelSerializer):
    comment = CommentSerializer(many=True)
    atachment = AttachmentSerializer()
    product_shop = ProductShopSerializer()
    shop = ShopSerializer()
    product = ProductSerializer()
    brand = BrandSerializer()

    class Meta:
        model = Category
        fields = "__all__"


class ProductRetrieveSerializer(ModelSerializer):
    comment = CommentSerializer(many=True)
    atachment = AttachmentSerializer()
    shop = ShopSerializer()
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductShopRetrieveSerializer(ModelSerializer):
    comment = CommentSerializer(many=True)
    atachment = AttachmentSerializer()
    shop = ShopSerializer()

    class Meta:
        model = ShopProduct
        fields = "__all__"


class AttachmentRetrieveSerializer(ModelSerializer):
    comment = CommentSerializer(many=True)
    product = ProductSerializer()
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Attachment
        fields = "__all__"


class CommentRetrieveSerializer(ModelSerializer):
    atachment = AttachmentSerializer()
    shop = ShopSerializer()
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Comment
        fields = "__all__"


class ShopRetrieveSerializer(ModelSerializer):
    comment = CommentSerializer(many=True)
    atachment = AttachmentSerializer()
    shop = ShopSerializer()
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Shop
        fields = "__all__"
