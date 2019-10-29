from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Shipment
from .serializers import ShipmentSerializer
from rest_framework import generics


def index(request):
    return HttpResponse('<h1>Weclome to Shipment</h1>')


class ShipmentList(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.values('pub_order_id', 'delivery_address')


class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

    def get_object(self):
        obj = get_object_or_404(Shipment, pub_order_id=self.kwargs.get('pub_order_id'))
        return obj






