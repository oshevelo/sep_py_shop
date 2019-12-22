import django_filters

from django_filters.rest_framework import FilterSet


class ProductByCategoryIdFilter(FilterSet):
    # filtering url e.g. /catalog/categories/products/?category_ids=1,2
    # /catalog/categories/products/?products_name=Book title&category_ids=1
    class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
        pass

    category_ids = NumberInFilter(field_name='id', lookup_expr='in')

    # e.g./catalog/categories/products/?products_name=Book title
    # ? How to NOT include not matching products ?
    products_name = django_filters.CharFilter(
        field_name='products__name', lookup_expr='iexact')
