# Generated by Django 4.1 on 2022-09-08 11:19

import json

from django.db import migrations


def create_default_categories(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    child_objects = []
    f = open('apps/common/fixtures/categories.json', encoding='utf-8')
    data = json.load(f)
    for key, value in data.items():
        parent = Category.objects.create(title=key, languages=value.get('languages', {}))
        for item in value.get('children'):
            child_objects.append(Category(title=item, parent=parent, languages=value.get('languages', {})))
    Category.objects.bulk_create(child_objects, ignore_conflicts=True)


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories)
    ]
