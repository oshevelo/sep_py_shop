from django_filters import rest_framework as filters

from rest_framework import generics

from apps.catalog.filters import ProductByCategoryIdFilter
from apps.catalog.models import Category
from apps.catalog.serializers import CategorySerializer, CategoryProductSerializer


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


class CategoryProductDetail(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductByCategoryIdFilter
