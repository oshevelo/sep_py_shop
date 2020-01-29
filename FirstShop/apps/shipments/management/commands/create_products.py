
from django.core.management.base import BaseCommand
from apps.products.models import Product
from django.utils import timezone
import csv
import random
import platform


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="path")

    def handle(self, *args, **options):
        path = options['path']
        try:
            data = csv.reader(open(path), delimiter=';')

            for row in data:
                if row[0] != "ISBN":
                    product = Product()
                    product.name = row[1]
                    product.price = random.random() * 100
                    product.available_count = random.randint(1, 100)
                    product.attributes = {
                        'ISBN': row[0],
                        'book_title': row[1],
                        'author': row[2],
                        'year-of-publication': row[3],
                        'publisher': row[4],
                        'small_image_URL': row[5],
                        'medium_image_URL': row[6],
                        'large_image_URL': row[7]
                    }
                    product.created = timezone.now()
                    product.updated = timezone.now()
                    product.save()
        except Exception as e:
            print(e)
