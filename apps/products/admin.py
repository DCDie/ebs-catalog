from django.contrib import admin

from apps.products.models import (
    Shop,
    Product,
    ProductShop,
    Attachment,
    Category,
    Comment,
)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'rating')


@admin.register(ProductShop)
class ProductShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'available', 'shop', 'product')


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'file_url', 'extension', 'file_size')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'shop', 'email', 'username', 'rating')
