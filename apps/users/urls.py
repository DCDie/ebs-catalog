from django.urls import path
from rest_framework_nested.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

from apps.users.views import UserViewSet

base_router = DefaultRouter(
    trailing_slash=False
)
base_router.register(
    prefix='users',
    viewset=UserViewSet,
    basename='users'
)

urlpatterns = base_router.urls

urlpatterns += [
    path(
        'token/refresh',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'users/login',
        TokenObtainPairView.as_view(),
        name='token_access'
    )
]