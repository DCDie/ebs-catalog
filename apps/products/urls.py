from rest_framework.routers import DefaultRouter

from apps.products.views import (
    CategoryViewSet,
    ProductViewSet,
    ProductShopViewSet,
    AttachmentViewSet,
    ShopViewSet,
    CommentViewSet,
    BrandViewSet
)

base_router = DefaultRouter(
    trailing_slash=False
)
base_router.register('categories', CategoryViewSet)
base_router.register('products', ProductViewSet)
base_router.register('shop_products', ProductShopViewSet)
base_router.register('attachments', AttachmentViewSet)
base_router.register('shops', ShopViewSet)
base_router.register('comments', CommentViewSet)
base_router.register('brands', BrandViewSet)

urlpatterns = base_router.urls
