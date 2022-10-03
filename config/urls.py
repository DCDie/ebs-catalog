from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# noinspection PyUnresolvedReferences
urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("", include("apps.products.urls")),
    path("", include("apps.users.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = [
        path("debug/", include("debug_toolbar.urls")),
    ] + urlpatterns
