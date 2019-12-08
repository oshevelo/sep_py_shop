import django_filters
from django.db.models import Q
from django_filters.rest_framework import FilterSet
from .models import Product 


class ProductFilter(FilterSet):

    def product_name_contains(self, qs, contains, value):
        return qs.filter(name__icontains=value)


    name = django_filters.filters.CharFilter(method='name_contains')


    class Meta:
        model = Product
        fields = ['id']

 