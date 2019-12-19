from django.core.management.base import BaseCommand, CommandError
from apps.orders.models import Order, OrderItem
from apps.shipments.models import Shipment, ShipmentLog
from django.utils import timezone
from django.contrib.auth.models import User
import requests
import json
import datetime

API_Key = 'b313e7c9662a02870c0d1b8a0cb9e683'


class Command(BaseCommand):
    def handle(self, *args, **options):
        params = {
            "apiKey": API_Key,
            "modelName": "TrackingDocument",
            "calledMethod": "getStatusDocuments",
            "methodProperties": {
                "Documents": [
                    {
                        "DocumentNumber": Shipment.objects.values_list('invoice_id', flat=True).get(public_id=1),
                        "Phone": Order.objects.values_list('phone', flat=True).get(public_id=1)
                    }
                ]
            }

        }

        response = requests.post('http://testapi.novaposhta.ua/v2.0/en/documentsTracking/json', json=params,
                                 headers={'Content-Type': 'application/json'})

        if response.status_code == 200:
            save_log(params, response)
            print(response.text)
        else:
            save_log(params, response)
            print(response.status_code)
