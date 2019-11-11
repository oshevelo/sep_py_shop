from rest_framework import serializers
from apps.orders.models import Order



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['public_id', 'user', 'phone', 'email', 'delivery', 'payment', 'status', 'date']


