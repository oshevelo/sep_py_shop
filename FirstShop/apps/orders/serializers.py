from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['public_order_id', 'user', 'phone', 'email', 'delivery_id', 'payment', 'status', 'date']