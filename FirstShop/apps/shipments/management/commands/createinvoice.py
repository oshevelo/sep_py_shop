
from django.core.management.base import BaseCommand, CommandError
from apps.orders.models import Order, OrderItem
from django.conf import settings
from apps.shipments.models import Shipment
from ._private import save_log
import requests
import datetime

API_Key = 'b313e7c9662a02870c0d1b8a0cb9e683'


class Command(BaseCommand):
    def handle(self, *args, **options):
        params = {
            "apiKey": API_Key,
            "modelName": "InternetDocument",
            "calledMethod": "save",
            "methodProperties":
                {
                    "NewAddress": "1",
                    "PayerType": "Sender",
                    "PaymentMethod": Order.objects.values_list('payment', flat=True).get(public_id=1),
                    "CargoType": "Cargo",
                    "VolumeGeneral": "0.1",
                    "Weight": "10",
                    "ServiceType": "WarehouseWarehouseDoors",
                    "SeatsAmount": OrderItem.objects.values_list('amount', flat=True).get(order=1),
                    "Description": 'Books',
                    "Cost": OrderItem.objects.values_list('price', flat=True).get(order_id=1),
                    "CitySender": settings.DELIVERY_DATA['CitySender'],
                    "Sender": settings.DELIVERY_DATA['Sender'],
                    "SenderAddress": settings.DELIVERY_DATA['SenderAddress'],
                    "ContactSender": settings.DELIVERY_DATA['ContactSender'],
                    "SendersPhone": settings.DELIVERY_DATA['SendersPhone'],
                    "RecipientCityName": Shipment.objects.values_list('delivery_address_city', flat=True).get(public_id=1),
                    "RecipientArea": Shipment.objects.values_list('delivery_address_area', flat=True).get(public_id=1),
                    "RecipientAreaRegions": Shipment.objects.values_list('delivery_address_area_region', flat=True).get(public_id=1),
                    "RecipientAddressName": Shipment.objects.values_list('delivery_address_street', flat=True).get(public_id=1),
                    "RecipientHouse": Shipment.objects.values_list('delivery_address_house', flat=True).get(public_id=1),
                    "RecipientFlat": Shipment.objects.values_list('delivery_address_flat', flat=True).get(public_id=1),
                    "RecipientName": Order.objects.values_list('user', flat=True).get(public_id=1),
                    "RecipientType": "PrivatePerson",
                    "RecipientsPhone": Order.objects.values_list('phone', flat=True).get(public_id=1),
                    "DateTime": datetime.datetime.today().strftime('%d.%m.%Y')
                }
        }
        response = requests.post('http://testapi.novaposhta.ua/v2.0/en/save_address/json', json=params,
                                 headers={'Content-Type': 'application/json'})

        if response.status_code == 200:
            save_log(params, response)
            print(response.text)
        else:
            save_log(params, response)
            print(response.status_code)



