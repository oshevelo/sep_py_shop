from django.shortcuts import get_object_or_404
from apps.delivery_api.models import Provider
from FirstShop.defs import *
from .serializers import DeliverySerializer
from rest_framework import generics


class DeliveryList(generics.ListCreateAPIView):
    serializer_class = DeliverySerializer
    queryset = Provider.objects.all()


class DeliveryTrack(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeliverySerializer
    queryset = Provider.objects.all()

    def get_object(self):
        obj = get_object_or_404(Provider, invoice_id=self.kwargs.get('invoice_id'))
        return obj


