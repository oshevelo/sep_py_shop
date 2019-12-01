from rest_framework import serializers
from .models import BaseShipment, Order

class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()s
    phone = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    date_of_order = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'phone', 'email', 'date_of_order']

# class OrderSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField()
#     phone = serializers.CharField(read_only=True)
#     email = serializers.CharField(read_only=True)
#     date_of_order = serializers.CharField(read_only=True)
#
#     class Meta:
#         model = Order
#         fields = ['id', 'phone', 'email', 'date_of_order']


class ShipmentSerializer(serializers.ModelSerializer):
    public_order = OrderSerializer()
 
    class Meta:
        model = BaseShipment
        fields = ('id', 'invoice_id', 'shipment_provider', 'delivery_address', 'shipment_status', 'public_order')

    def validate_public_order(self, data, *args, **kwargs):
        o = Order.objects.get(pk=data['id'])
        if o.my_shipment:
            raise serializers.ValidationError('here')
        return data

    def create(self, data, *args, **kwargs):
        order_id = data.pop('public_order')
        obj = super().create(data)
        o = Order.objects.get(pk=order_id['id'])
        obj.public_order = o
        obj.save()
        return obj
