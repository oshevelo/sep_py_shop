
from django.core.management.base import BaseCommand
from apps.shipments.models import ShipmentLog
from django.utils import timezone
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        or_id = input("Input order document number: ")
        params = {
            "OrderID": or_id,
        }
        try:
            int(or_id)
        except ValueError:
            print("Wrong order id type")
        else:
            response = requests.get('http://localhost:8000/delivery_api/'+or_id, headers={'format': 'json'}).text
            delivery_api_log = ShipmentLog()
            delivery_api_log.send_date = timezone.now()
            delivery_api_log.log_field = response
            delivery_api_log.request = params
            if response:
                delivery_api_log.is_processed = True
            else:
                delivery_api_log.is_processed = False
            delivery_api_log.save()

            print(response)

