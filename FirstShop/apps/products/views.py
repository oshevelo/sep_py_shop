from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer
from .models import Book 



class BookView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class SingleBookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
