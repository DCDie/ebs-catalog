from django.contrib import admin
from django.db.models import JSONField
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
    title = _('Category')
    parameter_name = 'parent_id'

    def lookups(self, request, model_admin):
        return [(category.pk, str(category)) for category in Category.objects.filter(parent__isnull=True)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(parent_id=int(self.value()))
        return queryset.all()


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
        'verified',
        'created_at',
        'modified_at'
    )
    list_filter = (
        'category',
        'rating',
        'verified'
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
        'verified',
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


@admin.register(ShopProduct)
class ProductShopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'price',
        'available',
        'shop',
        'product',
        'shop_category',
        'verified',
        'created_at',
        'modified_at'
    )
    list_filter = (
        'available',
        'verified'
    )
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
        'shop_category',
        'verified',
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
    list_filter = (
        CategoryParentListFilter,
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
        'modified_at',
    )
    list_select_related = (
        'parent',
    )
    ordering = (
        'title',
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


@admin.register(ShopCategory)
class ShopCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'shop',
        'category',
        'parent',
        'created_at',
        'modified_at'
    )
    search_fields = ('name',)
    fields = (
        'name',
        'shop',
        'category',
        'parent',
        'created_at',
        'modified_at'
    )
    readonly_fields = (
        'created_at',
        'modified_at'
    )
