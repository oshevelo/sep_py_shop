from django.core.management.base import BaseCommand, CommandError
from apps.orders.models import Order, OrderItem
from apps.shipments.models import BaseShipment
from django.contrib.auth.models import User
import requests
import json
import datetime

API_Key = 'b313e7c9662a02870c0d1b8a0cb9e683'


class Command(BaseCommand):
    def handle(self, *args, **options):
        getStatusDocuments = {
            "apiKey": API_Key,
            "modelName": "TrackingDocument",
            "calledMethod": "getStatusDocuments",
            "methodProperties": {
                "Documents": [
                    {
                        "DocumentNumber": BaseShipment.objects.values_list('invoice_id', flat=True).get(public_order_id=1),
                        "Phone": Order.objects.values_list('phone', flat=True).get(public_order=1)
                    }
                ]
            }

        }

        response = requests.post('https://api.novaposhta.ua/v2.0/json/', json=getStatusDocuments,
                                 headers={'Content-Type': 'application/json'}).text

        response = json.loads(response)
        res = response['data'][0]

        for i in res:
            print(i, res[i])