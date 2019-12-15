from django.http import HttpResponse
#from django.shortcuts import render

from django.shortcuts import get_object_or_404
from apps.orders.models import Order, OrderItem
from rest_framework import generics
from apps.orders.serializers import OrderSerializer
from rest_framework import filters


class Order_List_Create(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    search_fields = ['=email', 'phone', 'items__amount', 'items__price', 'items__discount']
    filter_backends = [filters.SearchFilter]


class Order_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


    def get_object(self):
        obj = get_object_or_404(Order, pk=self.kwargs.get('order_id'))
        return obj



class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)



# def account(request):
#     my_orders = Order.objects.filter(user=request.user)
#     return HttpResponse(my_orders)
