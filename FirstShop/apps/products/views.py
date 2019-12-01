from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer ComplectSerializer
from .models import Product, Complect



class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SingleProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ComplectView(ListCreateAPIView):
    queryset = Complect.objects.all()
    serializer_class = ComplectSerializer

class SingleComplectView(RetrieveUpdateDestroyAPIView):
    queryset = Complect.objects.all()
    serializer_class = ComplectSerializer
