from rest_framework import serializers
from polls.models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipment
        fields = (' pub_order_id', 'shipment_method', 'payment_method', 'delivery_addres')