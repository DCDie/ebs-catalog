from rest_framework.routers import DefaultRouter

from apps.products.views import (
    CategoryViewSet,
    ProductViewSet,
    ProductShopViewSet,
    AttachmentViewSet,
    ShopViewSet,
    CommentViewSet,
    BrandViewSet,
    ShopCategoryViewSet,
)

base_router = DefaultRouter(trailing_slash=False)
base_router.register(prefix="categories", viewset=CategoryViewSet, basename="categories")
base_router.register(prefix="products", viewset=ProductViewSet, basename="products")
base_router.register(prefix="shop-products", viewset=ProductShopViewSet, basename="shop_products")
base_router.register(prefix="attachments", viewset=AttachmentViewSet, basename="attachments")
base_router.register(prefix="shops", viewset=ShopViewSet, basename="shops")
base_router.register(prefix="comments", viewset=CommentViewSet, basename="comments")
base_router.register(prefix="brands", viewset=BrandViewSet, basename="brands")
base_router.register(prefix="shop-categories", viewset=ShopCategoryViewSet, basename="shop-categories")

urlpatterns = base_router.urls
