
from django.core.management.base import BaseCommand, CommandError
from apps.orders.models import Order, OrderItem
from django.conf import settings
from apps.shipments.models import Shipment
from ._private import save_log
import requests
import datetime

API_Key = 'b313e7c9662a02870c0d1b8a0cb9e683'


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--order', type=str, help="order")

    def handle(self, *args, **options):
        params = {
            "apiKey": API_Key,
            "modelName": "InternetDocument",
            "calledMethod": "save",
            "methodProperties":
                {
                    "NewAddress": "1",
                    "PayerType": "Sender",
                    "PaymentMethod": Order.objects.values_list('payment', flat=True).get(public_id=options['order']),
                    "CargoType": "Cargo",
                    "VolumeGeneral": "0.1",
                    "Weight": "10",
                    "ServiceType": "WarehouseWarehouseDoors",
                    "SeatsAmount": OrderItem.objects.values_list('amount', flat=True).get(order=options['order']),
                    "Description": 'Books',
                    "Cost": OrderItem.objects.values_list('price', flat=True).get(order_id=options['order']),
                    "CitySender": settings.DELIVERY_DATA['CitySender'],
                    "Sender": settings.DELIVERY_DATA['Sender'],
                    "SenderAddress": settings.DELIVERY_DATA['SenderAddress'],
                    "ContactSender": settings.DELIVERY_DATA['ContactSender'],
                    "SendersPhone": settings.DELIVERY_DATA['SendersPhone'],
                    "RecipientCityName": Shipment.objects.values_list('delivery_address_city', flat=True).get(public_id=options['order']),
                    "RecipientArea": Shipment.objects.values_list('delivery_address_area', flat=True).get(public_id=options['order']),
                    "RecipientAreaRegions": Shipment.objects.values_list('delivery_address_area_region', flat=True).get(public_id=options['order']),
                    "RecipientAddressName": Shipment.objects.values_list('delivery_address_street', flat=True).get(public_id=options['order']),
                    "RecipientHouse": Shipment.objects.values_list('delivery_address_house', flat=True).get(public_id=options['order']),
                    "RecipientFlat": Shipment.objects.values_list('delivery_address_flat', flat=True).get(public_id=options['order']),
                    "RecipientName": Order.objects.values_list('user', flat=True).get(public_id=options['order']),
                    "RecipientType": "PrivatePerson",
                    "RecipientsPhone": Order.objects.values_list('phone', flat=True).get(public_id=options['order']),
                    "DateTime": datetime.datetime.today().strftime('%d.%m.%Y')
                }
        }

        response = requests.post('{}'.format(settings.DELIVERY_API_HOST['create'], json=params, headers={'Content-Type': 'application/json'}))

        if response.status_code == 200:
            save_log(params, response)
            print(response.text)
        else:
            save_log(params, response)
            print(response.status_code)



