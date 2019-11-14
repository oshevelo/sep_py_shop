from rest_framework import serializers
from .models import BaseShipment, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['phone', 'email', 'date_of_order']


class ShipmentSerializer(serializers.ModelSerializer):
    public_order = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = BaseShipment
        fields = ('invoice_id', 'shipment_provider', 'delivery_address', 'shipment_status', 'public_order')


