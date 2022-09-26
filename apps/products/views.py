from requests import Response
from rest_framework.viewsets import (
    ModelViewSet,
    GenericViewSet
)

from apps.common.views import BaseViewSet
from apps.products.models import (
    Category,
    Shop,
    ShopProduct,
    Product,
    Comment,
    Attachment,
    Brand
)
from apps.products.serializers import (
    ProductShopSerializer,
    AttachmentSerializer,
    ShopSerializer,
    ProductSerializer,
    CommentSerializer,
    CategorySerializer,
    BrandSerializer, AttachmentRetrieveSerializer, CommentRetrieveSerializer, ProductRetrieveSerializer,
    ProductShopRetrieveSerializer, ShopRetrieveSerializer, CategoryRetrieveSerializer, BrandRetrieveSerializer,
)

__all__ = [
    'CategoryViewSet',
    'CommentViewSet',
    'AttachmentViewSet',
    'ShopViewSet',
    'ProductViewSet',
    'ProductShopViewSet',
    'BrandViewSet',
]


class CategoryViewSet(
    ModelViewSet,
    BaseViewSet

):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    serializer_by_action = dict(
        retrieve=CategoryRetrieveSerializer
    )


class ShopViewSet(
    ModelViewSet,

    BaseViewSet
):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    serializer_by_action = dict(
        retrieve=ShopRetrieveSerializer
    )


class ProductShopViewSet(
    ModelViewSet,

    BaseViewSet
):
    queryset = ShopProduct.objects.all()
    serializer_class = ProductShopSerializer
    serializer_by_action = dict(
        retrieve=ProductShopRetrieveSerializer
    )

class ProductViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    serializer_by_action = dict(
        retrieve=ProductRetrieveSerializer
    )

class AttachmentViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    serializer_by_action = dict(
        retrieve=AttachmentRetrieveSerializer
    )


class CommentViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    serializer_by_action = dict(
        retrieve=CommentRetrieveSerializer
    )


class BrandViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    serializer_by_action = dict(
        retrieve=BrandRetrieveSerializer
    )

