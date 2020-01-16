
from django.core.management.base import BaseCommand, CommandError
from apps.orders.models import Order, OrderItem
from apps.shipments.models import Shipment
from FirstShop.defs import SenderInfo
from django.contrib.auth.models import User
import requests
import json
import datetime

API_Key = 'b313e7c9662a02870c0d1b8a0cb9e683'


class Command(BaseCommand):
    def handle(self, *args, **options):
        params = {
            "apiKey": API_Key,
            "modelName": "InternetDocument",
            "calledMethod": "save",
            "methodProperties": {
            "NewAddress": "1",
            "PayerType": "Sender",
            "PaymentMethod": "Cash",
            "CargoType": "Cargo",
            "VolumeGeneral": "0.1",
            "Weight": "10",
            "ServiceType": "WarehouseDoors",
            "SeatsAmount": "1",
            "Description": "абажур",
            "Cost": "500",
            "CitySender": "8d5a980d-391c-11dd-90d9-001a92567626",
            "Sender": "5ace4a2e-13ee-11e5-add9-005056887b8d",
            "SenderAddress": "d492290b-55f2-11e5-ad08-005056801333",
            "ContactSender": "613b77c4-1411-11e5-ad08-005056801333",
            "SendersPhone": "380991234567",
            "RecipientCityName": "київ",
            "RecipientArea": "",
            "RecipientAreaRegions": "",
            "RecipientAddressName": "Столичне шосе",
            "RecipientHouse": "20",
            "RecipientFlat": "37",
            "RecipientName": "Тест Тест Тест",
            "RecipientType": "PrivatePerson",
            "RecipientsPhone": "380991234567",
            "DateTime": "25.09.2016"
            }
            }
        response = requests.post('https://api.novaposhta.ua/v2.0/json/', json=params,
                                 headers={'Content-Type': 'application/json'}).text
        return json.loads(response)


    def quaery(self, *args, **options):
        # p = BaseShipment.objects.get(public_order_id=1).only('invoice_id')
        p = Order.objects.values_list('phone', flat=True).get(public_order=1)
        print(p)
