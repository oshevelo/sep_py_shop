import django_filters
from django_filters.rest_framework import FilterSet


class CatalogProductFilter(FilterSet):
    # filtering url e.g. /catalog/categories/products/?category_ids=1,2
    # /catalog/categories/products/?product_name=Book title&category_ids=1
    class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
        pass

    category_ids = NumberInFilter(field_name='categories__id', lookup_expr='in', distinct=True)

    # e.g./catalog/categories/products/?product_name=Book title
    product_name = django_filters.CharFilter(
        field_name='name', lookup_expr='iexact')
