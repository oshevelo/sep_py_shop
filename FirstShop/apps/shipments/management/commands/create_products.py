
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
            data = csv.reader(open(path), delimiter=',')

            for row in data:
                if row[0] != "ISBN":
                    product = Product()
                    product.product_name = row[1]
                    product.product_price = random.random() * 100
                    product.product_avaliable_count = random.randint(1, 100)
                    product.product_detail = 'ISBN {} '.format(row[0])
                    product.product_can_be_sold = True
                    product.product_created_updated = timezone.now()
                    product.Publication_date = row[3]
                    product.Number_of_pages = random.randint(100, 1000)
                    product.product_autor = row[2]
                    product.publishing_house = row[4]
                    product.save()
        except Exception as e:
            print(e)