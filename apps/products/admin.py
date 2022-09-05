from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget

from apps.products.models import (
    Shop,
    Product,
    ProductShop,
    Attachment,
    Category,
    Comment,
    Brand,
)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_at',
        'modified_at'
    )
    search_fields = ('title',)
    fields = (
        'title',
        'description',
        'shop_detail',
        'language',
        'attachment',
        'created_at',
        'modified_at'
    )
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    readonly_fields = (
        'created_at',
        'modified_at'
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'category',
        'price',
        'rating',
        'created_at',
        'modified_at'
    )
    list_filter = (
        'category',
        'rating',
    )
    search_fields = (
        'title',
        'description'
    )
    fields = (
        'title',
        'description',
        'category',
        'specification',
        'language',
        'price',
        'rating',
        'attachments',
        'created_at',
        'modified_at'
    )
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    readonly_fields = (
        'created_at',
        'modified_at'
    )


@admin.register(ProductShop)
class ProductShopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'price',
        'available',
        'shop',
        'product',
        'created_at',
        'modified_at'
    )
    list_filter = ('available',)
    search_fields = (
        'title',
        'description'
    )
    fields = (
        'title',
        'description',
        'price',
        'available',
        'attachment',
        'shop',
        'language',
        'product',
        'created_at',
        'modified_at'
    )
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    readonly_fields = (
        'created_at',
        'modified_at'
    )


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'file_url',
        'extension',
        'file_size',
        'created_at',
        'modified_at'
    )
    list_filter = ('extension',)
    search_fields = (
        'title',
        'file_url'
    )
    fields = (
        'title',
        'file_url',
        'extension',
        'file_size',
        'language',
        'created_at',
        'modified_at'
    )
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    readonly_fields = (
        'created_at',
        'modified_at'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'parent',
        'created_at',
        'modified_at'
    )
    search_fields = (
        'title',
    )
    fields = (
        'title',
        'parent',
        'attachment',
        'language',
        'created_at',
        'modified_at'
    )
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    readonly_fields = (
        'created_at',
        'modified_at'
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'shop',
        'user',
        'rating',
        'created_at',
        'modified_at'
    )
    list_filter = (
        'rating',
    )
    search_fields = (
        'text',
    )
    fields = (
        'text',
        'product',
        'shop',
        'user',
        'language',
        'rating',
        'created_at',
        'modified_at'
    )
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    readonly_fields = (
        'created_at',
        'modified_at'
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'parent',
        'created_at',
        'modified_at'
    )
    search_fields = (
        'title',
    )
    fields = (
        'title',
        'parent',
        'created_at',
        'modified_at'
    )
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    readonly_fields = (
        'created_at',
        'modified_at'
    )
