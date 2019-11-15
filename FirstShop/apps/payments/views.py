from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404
from apps.payments.models import Payment
from rest_framework import generics
from apps.payments.serializers import PaymentSerializer


def index(request):
    return HttpResponse('Hi!!!!!!')

'''
class Payment_list(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class Payment_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_object(self):
        obj = get_object_or_404(Payment, pk=self.kwargs.get('payment_id'))
        return obj
'''
