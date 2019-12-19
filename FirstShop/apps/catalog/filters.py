import django_filters

from django_filters.rest_framework import FilterSet


class ProductByCategoryIdFilter(FilterSet):
    # filtering url e.g. /catalog/categories/products/?category_ids=1,2
    class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
        pass

    category_ids = NumberInFilter(field_name='id', lookup_expr='in')
