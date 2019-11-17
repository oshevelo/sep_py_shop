from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from apps.orders.models import Order, OrderItem
from rest_framework import generics
from apps.orders.serializers import OrderSerializer, OrderItemSerializer


class Order_List_Create(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Order_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs.get('order_id'))
        return obj

class Order_Item_List_Create(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class Order_Item_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def get_object(self):
        obj = get_object_or_404(OrderItem, pk=self.kwargs.get('order_item_id'))
        return obj

