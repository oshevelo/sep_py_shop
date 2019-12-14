from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import get_object_or_404
from apps.carts.models import Cart
from rest_framework import generics
from apps.carts.serializers import CartSerializer


def index(request):
    return  HttpResponse("Hello, World!")


class Cart_List(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class Cart_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        obj = get_object_or_404(Cart, pk=self.kwargs.get('cart_id'))
        return obj
