from django.shortcuts import get_object_or_404, render
from .models import BaseShipment
from .serializers import ShipmentSerializer
from rest_framework import generics

city = 'Kyiv'
branch = 'Branch #1'
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


def create_invoice():
    params = {
        "apiKey": API_Key,
        "modelName": "InternetDocument",
        "calledMethod": "save",
        "methodProperties": {
            "IsTakeAttorney": "1",
            "PayerType": "Sender",
            # "PaymentMethod": Payments.payment_method,
            "DateTime": DateToReceive,
            "CargoType": "Cargo",
            "VolumeGeneral": "0.1",
            "Weight": "10",
            "ServiceType": "WarehouseDoors",
            "SeatsAmount": "1",
            "Description": OrderItem.order,
            "Cost": OrderItem.price,
            "CitySender": city,
            "Sender": User.get_full_name,
            "SenderAddress": BaseShipment.delivery_address,
            "ContactSender": User.email,
            "SendersPhone": "380678734567",
            "CityRecipient": 'Kyiv',
            "Recipient": 'FirstShop',
            "RecipientAddress": 'Kyiv',
            "ContactRecipient": 'FirstShopAddress',
            "RecipientsPhone": "380631112223"
        }
    }
    r = requests.post('https://api.novaposhta.ua/v2.0/json/', json=params,
                      headers={'Content-Type': 'application/json'}).text
    return json.loads(r)
