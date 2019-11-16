from django.shortcuts import get_object_or_404
from .models import BaseShipment
from .serializers import ShipmentSerializer
from FirstShop.variables import *
from rest_framework import generics


class ShipmentList(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = BaseShipment.objects.all()


class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer
    queryset = BaseShipment.objects.all()

    def get_object(self):
        obj = get_object_or_404(BaseShipment, pk=self.kwargs.get('public_order_id'))
