from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import (
    ModelViewSet
)

from rest_framework import filters
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
    ordering_fields = ['id', 'title']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    filterset_fields = ['parent']

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
    ordering_fields = ['id']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', ]

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
    ordering_fields = ['id', 'title', 'created_at', 'modified_at', 'price', 'attachmXents', 'shop', 'shop_category']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['shop', 'shop_category', 'product']

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
    ordering_fields = ['id', 'title', 'created_at', 'modified_at', 'price']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    filterset_fields = ['price']

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
    ordering_fields = ['id', 'title', 'created_at', 'modified_at']
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'file_url']
    filterset_fields = ['price']


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
    ordering_fields = ['id', 'product', 'created_at', 'modified_at', 'shop', 'user']
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']
    filterset_fields = ['shop', 'shop_category']

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
    ordering_fields = ['id', 'product', 'created_at', 'modified_at', 'shop', 'user']
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']
    filterset_fields = ['parent']

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
    ordering_fields = ['id', 'shop', 'created_at', 'modified_at', 'category']
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    filterset_fields = ['category','shop','parent']

    def get_queryset(self):
        queryset = super(ShopCategoryViewSet, self).get_queryset()
        if self.action == 'retrieve':
            return queryset.select_related(
                'shop',
                'category'
            )
        return queryset
