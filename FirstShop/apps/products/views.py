from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
from .models import Product 
from .filters import ProductFilter


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter

    def get_queryset(self, *args, **kwargs):
        if self.request.GET.get('search'):
            return Product.objects.filter(product_name__icontains=self.request.GET.get('search'))
        return Product.objects.all()


class SingleProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
