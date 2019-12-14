from django.shortcuts import get_object_or_404
from apps.orders.models import Order
from apps.shipments.models import Shipment
from apps.shipments.serializers import ShipmentSerializer, OrderSerializer
from FirstShop.defs import *
from rest_framework import generics, filters


class ShipmentList(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'invoice_id', 'shipment_provider', 'delivery_address', 'shipment_status']


class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs.get('public_id'))
        return obj


