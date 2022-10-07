from django.contrib import admin
from django.db.models import JSONField, Q
from django.utils.translation import gettext_lazy as _
from django_json_widget.widgets import JSONEditorWidget

from apps.products.models import (
    Shop,
    Product,
    ShopProduct,
    Attachment,
    Category,
    Comment,
    Brand,
    ShopCategory,
)


class CategoryParentListFilter(admin.SimpleListFilter):
    title = _("Category")
    parameter_name = "parent_id"

    def lookups(self, request, model_admin):
        return [
            (category.pk, str(category))
            for category in Category.objects.filter(parent__isnull=True)
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(parent_id=int(self.value()))
        return queryset.all()


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "modified_at")
    search_fields = ("title",)
    fields = (
        "title",
        "description",
        "shop_detail",
        "languages",
        "attachments",
        "created_at",
        "modified_at",
    )
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
    readonly_fields = ("created_at", "modified_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "price",
        "rating",
        "verified",
        "created_at",
        "modified_at",
    )
    list_filter = ("category", "rating", "verified")
    search_fields = ("title", "description")
    fields = (
        "title",
        "description",
        "category",
        "specification",
        "languages",
        "price",
        "rating",
        "attachments",
        "verified",
        "created_at",
        "modified_at",
    )
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
    readonly_fields = ("created_at", "modified_at")


@admin.register(ShopProduct)
class ProductShopAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "price",
        "available",
        "shop",
        "product",
        "shop_category",
        "verified",
        "created_at",
        "modified_at",
    )
    list_filter = ("available", "verified")
    search_fields = ("title", "description")
    fields = (
        "title",
        "description",
        "price",
        "available",
        "attachments",
        "shop",
        "languages",
        "product",
        "shop_category",
        "verified",
        "created_at",
        "modified_at",
    )
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
    readonly_fields = ("created_at", "modified_at")


class ExtensionListFilter(admin.SimpleListFilter):
    title = 'File extension'
    parameter_name = 'file_extension'

    def lookups(self, request, model_admin):
        return (
            ('.jpg', '.jpg'),
            ('.png', '.png'),
            ('.pdf', '.pdf'),
            ('.xlsx', '.xlsx'),
            ('.doc', '.doc'),
            ('.exe', '.exe'),
            ('.txt', '.txt'),
            ('.csv', '.csv'),
            ('other', 'other'),
        )

    def queryset(self, request, queryset):
        if self.value():
            if self.value() == 'other':
                return queryset.filter(
                    ~Q(extension='.jpg') & ~Q(extension='.pdf') & ~Q(
                        extension='.png') & ~Q(extension='.xlsx') & ~Q(
                        extension='.doc') & ~Q(extension='.exe') & ~Q(
                        extension='.txt') & ~Q(extension='.csv'))
            return queryset.filter(extension=self.value())
        return queryset


class SizeListFilter(admin.SimpleListFilter):
    title = 'File size'
    parameter_name = 'file_size'

    def lookups(self, request, model_admin):
        return (
            ('<1MB', '<1MB'),
            ('1MB-5Mb', '1MB - 5Mb'),
            ('>5Mb', '>5Mb'),
        )

    def queryset(self, request, queryset):
        if self.value() == '<1MB':
            return queryset.filter(
                file_size__lt=1_048_576
            )
        if self.value() == '1MB-5Mb':
            return queryset.filter(
                file_size__gte=1_048_576,
                file_size__lte=5_242_880
            )
        if self.value() == '>5Mb':
            return queryset.filter(
                file_size__gt=5_242_880
            )


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "file_url",
        "extension",
        "file_size",
        "created_at",
        "modified_at",
    )
    list_filter = (ExtensionListFilter, SizeListFilter)
    search_fields = ("title", "file_url")
    fields = (
        "title",
        "file_url",
        "extension",
        "file_size",
        "languages",
        "created_at",
        "modified_at",
    )
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
    readonly_fields = ("created_at", "modified_at")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "parent", "created_at", "modified_at")
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title",)
    list_filter = (CategoryParentListFilter,)
    fields = (
        "title",
        "parent",
        "attachments",
        "languages",
        "created_at",
        "modified_at",
    )
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
    readonly_fields = (
        "created_at",
        "modified_at",
    )
    list_select_related = ("parent",)
    ordering = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "shop",
        "user",
        "rating",
        "created_at",
        "modified_at",
    )
    list_filter = ("rating",)
    search_fields = ("text",)
    fields = (
        "text",
        "product",
        "shop",
        "user",
        "languages",
        "attachments",
        "rating",
        "created_at",
        "modified_at",
    )
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
    readonly_fields = ("created_at", "modified_at")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "parent", "created_at", "modified_at")
    search_fields = ("title",)
    fields = ("title", "parent", "attachments", "created_at", "modified_at")
    formfield_overrides = {
        JSONField: {"widget": JSONEditorWidget},
    }
    readonly_fields = ("created_at", "modified_at")


@admin.register(ShopCategory)
class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "shop",
        "category",
        "parent",
        "created_at",
        "modified_at",
    )
    search_fields = ("name",)
    fields = ("name", "shop", "category", "parent", "created_at", "modified_at")
    readonly_fields = ("created_at", "modified_at")
