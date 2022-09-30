from rest_framework.serializers import ModelSerializer

from apps.products.models import (
    Category,
    Comment,
    Shop,
    Attachment,
    ShopProduct,
    Product,
    Brand,
    ShopCategory,
)

__all__ = [
    "CategorySerializer",
    "CommentSerializer",
    "ShopSerializer",
    "ProductSerializer",
    "AttachmentSerializer",
    "ProductShopSerializer",
    "BrandSerializer",
    "ShopCategorySerializer",
    "BrandRetrieveSerializer",
    "CategoryRetrieveSerializer",
    "CommentRetrieveSerializer",
    "ProductRetrieveSerializer",
    "ProductShopRetrieveSerializer",
    "ShopRetrieveSerializer",
    "ShopCategoryRetrieveSerializer",
]


# noinspection DuplicatedCode
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


# noinspection DuplicatedCode
class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"


class ProductShopSerializer(ModelSerializer):
    class Meta:
        model = ShopProduct
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ShopCategorySerializer(ModelSerializer):
    class Meta:
        model = ShopCategory
        fields = "__all__"


class ShopCategoryRetrieveSerializer(ModelSerializer):
    shop = ShopSerializer()
    category = CategorySerializer()

    class Meta:
        model = ShopCategory
        fields = "__all__"


class BrandRetrieveSerializer(ModelSerializer):
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Brand
        fields = "__all__"


class CategoryRetrieveSerializer(ModelSerializer):
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"


class ProductRetrieveSerializer(ModelSerializer):
    category = CategorySerializer(many=True)
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductShopRetrieveSerializer(ModelSerializer):
    category = CategorySerializer(many=True)
    attachments = AttachmentSerializer(many=True)
    shop = ShopSerializer()
    product = ProductSerializer()
    shop_category = ShopCategorySerializer()

    class Meta:
        model = ShopProduct
        fields = "__all__"


class CommentRetrieveSerializer(ModelSerializer):
    product = ProductSerializer()
    shop = ShopSerializer()
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Comment
        fields = "__all__"


class ShopRetrieveSerializer(ModelSerializer):
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Shop
        fields = "__all__"
