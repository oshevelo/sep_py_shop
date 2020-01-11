from django.shortcuts import get_object_or_404
from apps.orders.models import Order
from apps.shipments.models import Shipment
from apps.shipments.serializers import ShipmentSerializer, OrderSerializer
from FirstShop.defs import *
from rest_framework import generics, filters


class ShipmentList(generics.ListCreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id']


class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs.get('public_id'))
        return obj
