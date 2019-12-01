from django.shortcuts import get_object_or_404
from apps.orders.models import Order
from apps.shipments.models import Shipment
from apps.shipments.serializers import ShipmentSerializer
from FirstShop.defs import *
from rest_framework import generics


class ShipmentList(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

    def get_object(self):
        obj = get_object_or_404(Shipment, pk=self.kwargs.get('public_id_id'))
        return obj
