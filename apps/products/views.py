from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.products.models import (
    Category,
    Shop,
    ProductShop,
    Product,
    Comment,
    Attachment
)
from apps.products.serializers import (
    ProductShopSerializer,
    AttachmentSerializer,
    ShopSerializer,
    ProductSerializer,
    CommentSerializer,
    CategorySerializer,
)

__all__ = [
    'CategoryViewSet',
    'CommentViewSet',
    'AttachmentViewSet',
    'ShopViewSet',
    'ProductViewSet',
    'ProductShopViewSet'
]


class CategoryViewSet(
    ModelViewSet,
    GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ShopViewSet(
    ModelViewSet,
    GenericViewSet
):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductShopViewSet(
    ModelViewSet,
    GenericViewSet
):
    queryset = ProductShop.objects.all()
    serializer_class = ProductShopSerializer


class ProductViewSet(
    ModelViewSet,
    GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AttachmentViewSet(
    ModelViewSet,
    GenericViewSet
):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class CommentViewSet(
    ModelViewSet,
    GenericViewSet
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
