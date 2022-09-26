from rest_framework.viewsets import (
    ModelViewSet,
    GenericViewSet
)

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
    BrandSerializer,
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
    queryset = ShopProduct.objects.all()
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


class BrandViewSet(
    ModelViewSet,
    GenericViewSet
):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    # def test_comments_retriew(self):
    #     comment = Comment.objects.create()
    #     response = self.client.get(f'/products/{product.id}/')
    #     self.assertEqual(HTTP_200_OK, response.status_code)
