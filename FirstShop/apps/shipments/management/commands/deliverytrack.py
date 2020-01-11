from django.core.management.base import BaseCommand, CommandError
from apps.orders.models import Order, OrderItem
from apps.shipments.models import Shipment, ShipmentLog
from django.conf import settings
from ._private import save_log
import requests

API_Key = 'b313e7c9662a02870c0d1b8a0cb9e683'


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--order', type=int, help="order")

    def handle(self, *args, **options):
        params = {
            "apiKey": API_Key,
            "modelName": "TrackingDocument",
            "calledMethod": "getStatusDocuments",
            "methodProperties": {
                "Documents": [
                    {
                        "DocumentNumber": Shipment.objects.values_list('invoice_id', flat=True).get(public_id=options['order']),
                        "Phone": Order.objects.values_list('phone', flat=True).get(public_id=options['order'])
                    }
                ]
            }

        }

        response = requests.post('{}'.format(settings.DELIVERY_API_HOST['track']), json=params,
                                 headers={'Content-Type': 'application/json'})

        if response.status_code == 200:
            save_log(params, response)
            print(response.text)
        else:
            save_log(params, response)
            print(response.status_code)
