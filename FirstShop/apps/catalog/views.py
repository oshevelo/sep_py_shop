from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from apps.catalog.models import Category
from apps.catalog.serializers import CategorySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
