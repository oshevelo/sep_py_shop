from rest_framework import serializers
from .models import BaseShipment


class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseShipment
        fields = ('pub_order_id', 'shipment_method', 'payment_method', 'delivery_address')
