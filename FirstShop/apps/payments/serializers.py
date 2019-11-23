from rest_framework import serializers
from .models import Payment, BillingLogs


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'payment_id', 'product', 'amount', 'date', 'provider']
