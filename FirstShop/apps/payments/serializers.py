from rest_framework import serializers
from .models import Payment, BillingLogs


class BillingLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingLogs
        fields = ['payment_date', 'status', 'data']


class PaymentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Payment
        fields = ['id', 'user', 'payment_id', 'product', 'amount', 'date', 'provider']
