from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from apps.catalog.models import Category
from apps.catalog.serializers import CategorySerializer


# TBD Why not possible create generics.ListCreateAPIView
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# TBD The same ? generics.RetrieveUpdateDestroyAPIView
class CategoryDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
