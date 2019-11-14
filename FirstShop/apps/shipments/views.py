from django.shortcuts import get_object_or_404, render
from .models import BaseShipment
from .serializers import ShipmentSerializer
from FirstShop.variables import *
from rest_framework import generics


def index(request):
    deliveries = BaseShipment.objects.values('public_order_id', 'delivery_address')
    return render(request, 'shipments/index.html', context={'Shipments': deliveries})


class ShipmentList(generics.ListAPIView):
    serializer_class = ShipmentSerializer
    queryset = BaseShipment.objects.values('public_order_id', 'delivery_address', 'shipment_status', 'status_change_date')


class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer
    queryset = BaseShipment.objects.all()

    def get_object(self):
        obj = get_object_or_404(BaseShipment, public_order=self.kwargs.get('public_order_id'))




