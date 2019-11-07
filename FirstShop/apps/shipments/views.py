from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from .models import BaseShipment, Order, OrderItem
from .serializers import ShipmentSerializer
from rest_framework import generics
import requests
import json
import datetime

SenderCity = 'Kyiv'
SenderPhone = '+380634338963'
Senderbranch = 'Branch #1'
DateToReceive = '01-12-2019 12:00:00'
DateReceived = '02-12-2019 12:00:00'
API_Key = 'b313e7c9662a02870c0d1b8a0cb9e683'


def index(request):
    deliveries = BaseShipment.objects.all()
    return render(request, 'base.html', context={'Shipments': deliveries})


class ShipmentList(generics.ListAPIView):
    serializer_class = ShipmentSerializer
    queryset = BaseShipment.objects.values('pub_order_id', 'delivery_address')


class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer
    queryset = BaseShipment.objects.all()

    def get_object(self):
        obj = get_object_or_404(BaseShipment, pub_order_id=self.kwargs.get('pub_order_id'))


def create_invoice(request):
    params = {
        "apiKey": API_Key,
        "modelName": "InternetDocument",
        "calledMethod": "save",
        "methodProperties":
            {
                "NewAddress": "1",
                "PayerType": "Sender",
                "PaymentMethod": BaseShipment.payment_method,
                "CargoType": "Cargo",
                "VolumeGeneral": "0.1",
                "Weight": "10",
                "ServiceType": "WarehouseWarehouse",
                "SeatsAmount": OrderItem.amount,
                "Description": OrderItem.description,
                "Cost": OrderItem.price,
                "CitySender": "8d5a980d-391c-11dd-90d9-001a92567626",
                "Sender": "5ace4a2e-13ee-11e5-add9-005056887b8d",
                "SenderAddress": "d492290b-55f2-11e5-ad08-005056801333",
                "ContactSender": "613b77c4-1411-11e5-ad08-005056801333",
                "SendersPhone": SenderPhone,
                "RecipientCityName": SenderCity,
                "RecipientArea": "",
                "RecipientAreaRegions": "",
                "RecipientAddressName": "1",
                "RecipientHouse": "",
                "RecipientFlat": "",
                "RecipientName": User.get_full_name,
                "RecipientType": "PrivatePerson",
                "RecipientsPhone": User.email,
                "DateTime": datetime.datetime.today().strftime('%d.%m.%Y')
            }
    }
    response = requests.post('https://api.novaposhta.ua/v2.0/json/', json=params,
                      headers={'Content-Type': 'application/json'}).text
    return render(request, 'base.html', context=json.loads(response))


def track_delivery(request):

    getStatusDocuments = {
        "apiKey": API_Key,
        "modelName": "TrackingDocument",
        "calledMethod": "getStatusDocuments",
        "methodProperties": {
            "Documents": [
                {
                    "DocumentNumber": BaseShipment.invoice_id,
                    "Phone": User.phone
                }
            ]
        }

    }

    response = requests.post('https://api.novaposhta.ua/v2.0/json/', json=getStatusDocuments, headers={'Content-Type': 'application/json'}).text

    return render(request, 'base.html', context=json.loads(response))
