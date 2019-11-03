from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from apps.orders.models import Order
from rest_framework import generics
from apps.orders.serializers import OrderSerializer


def index(request):
    return HttpResponse("Hello, world")


class Order_List(generics.ListAPIView): # ми просто виведимо список  всіх питань
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Order_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs.get('public_order_id'))
        return obj
