from django_filters import rest_framework as filters

from rest_framework import generics

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

    def get_queryset(self, *args, **kwargs):
        # e.g. /catalog/categories/products/?category_ids=1,2
        category_ids_str = self.request.GET.get('category_ids')
        category_ids = [int(category_id) for category_id in category_ids_str.split(',')]

        return Category.objects.filter(id__in=category_ids)
