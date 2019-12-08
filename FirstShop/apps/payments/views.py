from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Payment
from rest_framework import generics
from .serializers import PaymentSerializer


class Payment_list(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class Payment_Detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def get_object(self):
        obj = get_object_or_404(Payment, pk=self.kwargs.get('id'))
        return obj
