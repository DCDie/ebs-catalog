from pathlib import Path

from auditlog.registry import auditlog
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

__all__ = [
    'Comment',
    'Category',
    'ProductShop',
    'Product',
    'Shop',
    'Attachment'
]


class Category(models.Model):
    title = models.CharField(
        max_length=155
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )
    language = models.JSONField(
        blank=True,
        null=True
    )
    attachment = models.ManyToManyField(
        'Attachment',
        related_name='category_attachment',
        blank=True
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(
        max_length=155
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    specification = models.JSONField(
        blank=True,
        null=True
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    language = models.JSONField(
        blank=True,
        null=True
    )
    rating = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    attachment = models.ManyToManyField(
        'Attachment',
        related_name='product_attachment',
        blank=True
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    shop = models.ForeignKey(
        'Shop',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    email = models.EmailField()
    username = models.CharField(
        max_length=50
    )
    language = models.JSONField(
        blank=True,
        null=True
    )
    rating = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.id}'


class Shop(models.Model):
    title = models.CharField(
        max_length=155
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    shop_detail = models.JSONField(
        null=True,
        blank=True
    )
    language = models.JSONField(
        blank=True,
        null=True
    )
    attachment = models.ManyToManyField(
        'Attachment',
        related_name='shop_attachment',
        blank=True
    )

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.title


class ProductShop(models.Model):
    title = models.CharField(
        max_length=155
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    available = models.BooleanField(
        default=True
    )
    attachment = models.ManyToManyField(
        'Attachment',
        related_name='product_shop_attachment'
    )
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE
    )
    language = models.JSONField(
        blank=True,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Shop product'
        verbose_name_plural = 'Shop products'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(
        max_length=155,
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    language = models.JSONField(
        blank=True,
        null=True
    )


class Attachment(models.Model):
    title = models.CharField(
        max_length=75,
    )
    file_url = models.FileField(
        blank=True
    )
    extension = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    file_size = models.IntegerField(
        blank=True,
        null=True
    )
    language = models.JSONField(
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.file_size = self.file_url.size
        self.extension = Path(self.file_url.name).suffix
        super(Attachment, self).save(force_insert, force_update, using, update_fields)


# Register models to auditlog
auditlog.register(Brand)
