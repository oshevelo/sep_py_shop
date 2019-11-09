from django.shortcuts import get_object_or_404, render
from .models import BaseShipment
from .serializers import ShipmentSerializer
from rest_framework import generics


def index(request):
    deliveries = BaseShipment.objects.all()
    return render(request, 'base.html', context={'Shipments': deliveries})


class ShipmentList(generics.ListAPIView):
    serializer_class = ShipmentSerializer
    queryset = BaseShipment.objects.values('public_order', 'delivery_address')


class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer
    queryset = BaseShipment.objects.all()

    def get_object(self):
        obj = get_object_or_404(BaseShipment, public_order=self.kwargs.get('public_order'))


