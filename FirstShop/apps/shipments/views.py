from django.shortcuts import get_object_or_404, render
from .models import Shipment
from .serializers import ShipmentSerializer
from rest_framework import generics


def index(request):
    deliveries = Shipment.objects.all()
    return render(request, 'base.html', context={'Shipments': deliveries})


class ShipmentList(generics.ListAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.values('pub_order_id', 'delivery_address')


class ShipmentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()

    def get_object(self):
        obj = get_object_or_404(Shipment, pub_order_id=self.kwargs.get('pub_order_id'))
        return obj
