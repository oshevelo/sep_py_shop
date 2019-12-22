from apps.catalog.filters import CatalogProductFilter
from apps.catalog.models import Category
from apps.catalog.serializers import CategoryProductSerializer, CategorySerializer
from apps.products.models import Product
from django_filters import rest_framework as filters
from rest_framework import generics


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = [filters.DjangoFilterBackend]
    # /catalog/categories/?category_name=parent1
    filterset_fields = ['category_name']


# TBD The same ? generics.RetrieveUpdateDestroyAPIView
class CategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CategoryProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CatalogProductFilter
