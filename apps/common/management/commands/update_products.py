from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Update content fields"

    # pylint: disable=unused-argument
    def handle(self, *args, **options):
        from apps.common.parsers.insert_db import InsertDataBase

        inserter = InsertDataBase()
        inserter.add_shop_category()
        print("Categories are updated")
        inserter.add_shop_products()
        print("Products are updated")
