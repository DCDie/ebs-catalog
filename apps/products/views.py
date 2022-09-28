from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import (
    ModelViewSet
)

from apps.common.views import BaseViewSet
from apps.products.models import (
    Category,
    Shop,
    ShopProduct,
    Product,
    Comment,
    Attachment,
    Brand,
    ShopCategory,
)
from apps.products.serializers import (
    ProductShopSerializer,
    AttachmentSerializer,
    ShopSerializer,
    ProductSerializer,
    CommentSerializer,
    CategorySerializer,
    BrandSerializer,
    ShopCategorySerializer,
    CommentRetrieveSerializer,
    ProductShopRetrieveSerializer,
    ShopRetrieveSerializer,
    CategoryRetrieveSerializer,
    BrandRetrieveSerializer,
    ProductRetrieveSerializer,
    ShopCategoryRetrieveSerializer
)

__all__ = [
    'CategoryViewSet',
    'CommentViewSet',
    'AttachmentViewSet',
    'ShopViewSet',
    'ProductViewSet',
    'ProductShopViewSet',
    'BrandViewSet',
    'ShopCategoryViewSet',
]


class CategoryViewSet(
    ModelViewSet,
    BaseViewSet

):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    serializer_by_action = dict(
        retrieve=CategoryRetrieveSerializer
    )

    def get_queryset(self):
        queryset = super(CategoryViewSet, self).get_queryset()
        if self.action == 'retrieve':
            return queryset.prefetch_related('attachments')
        return queryset


class ShopViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsAuthenticated,)
    serializer_by_action = dict(
        retrieve=ShopRetrieveSerializer
    )

    def get_queryset(self):
        queryset = super(ShopViewSet, self).get_queryset()
        if self.action == 'retrieve':
            return queryset.prefetch_related('attachments')
        return queryset


class ProductShopViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = ShopProduct.objects.all()
    serializer_class = ProductShopSerializer
    permission_classes = (IsAuthenticated,)
    serializer_by_action = dict(
        retrieve=ProductShopRetrieveSerializer
    )

    def get_queryset(self):
        queryset = super(ProductShopViewSet, self).get_queryset()
        if self.action == 'retrieve':
            return queryset.select_related(
                'shop',
                'product',
                'shop_category'
            ).prefetch_related(
                'category',
                'attachments'
            )
        return queryset


class ProductViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    serializer_by_action = dict(
        retrieve=ProductRetrieveSerializer
    )

    def get_queryset(self):
        queryset = super(ProductViewSet, self).get_queryset()
        if self.action == 'retrieve':
            return queryset.prefetch_related(
                'category',
                'attachments'
            )
        return queryset


class AttachmentViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super(AttachmentViewSet, self).get_queryset()
        if self.action == 'retrieve':
            queryset.select_related()
        return queryset


class CommentViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    serializer_by_action = dict(
        retrieve=CommentRetrieveSerializer
    )

    def get_queryset(self):
        queryset = super(CommentViewSet, self).get_queryset()
        if self.action == 'retrieve':
            return queryset.select_related(
                'product',
                'shop'
            ).prefetch_related(
                'attachments'
            )
        return queryset


class BrandViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated,)
    serializer_by_action = dict(
        retrieve=BrandRetrieveSerializer
    )

    def get_queryset(self):
        queryset = super(BrandViewSet, self).get_queryset()
        if self.action == 'retrieve':
            return queryset.prefetch_related(
                'attachments'
            )
        return queryset


class ShopCategoryViewSet(
    ModelViewSet,
    BaseViewSet
):
    queryset = ShopCategory.objects.all()
    serializer_class = ShopCategorySerializer
    permission_classes = (IsAuthenticated,)
    serializer_by_action = dict(
        retrieve=ShopCategoryRetrieveSerializer
    )

    def get_queryset(self):
        queryset = super(ShopCategoryViewSet, self).get_queryset()
        if self.action == 'retrieve':
            return queryset.select_related(
                'shop',
                'category'
            )
        return queryset
