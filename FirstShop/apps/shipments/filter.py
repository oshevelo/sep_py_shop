import django_filters
from django_filters.rest_framework import FilterSet
from .models import Shipment


class ShipmentsFilter(FilterSet):

    def shipments_adress_contains(self, qs, contains, value):
        return qs.filter(name__icontains=value)

    shipments_address = django_filters.filters.CharFilter(method='shipments_adress_contains')

    class Meta:
        model = Shipment
        fields = ['public_id']