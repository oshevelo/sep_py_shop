from rest_framework import serializers, validators
from apps.orders.models import Order
from apps.shipments.models import Shipment


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    phone = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    date_of_order = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'phone', 'email', 'date_of_order']


class ShipmentSerializer(serializers.ModelSerializer):
    public_id = OrderSerializer()
 
    class Meta:
        model = Shipment
        fields = ['id', 'invoice_id', 'shipment_provider', 'delivery_address', 'shipment_status', 'public_id']

    def validate_public_id(self, data, *args, **kwargs):
        check_order = Order.objects.filter(pk=data['id']).first()
        
        if not check_order:
            raise serializers.ValidationError('Wrong Order Id. Select other ID or create new one')

        o = Order.objects.get(pk=data['id'])
        if o.my_shipment:
            raise serializers.ValidationError('More then one order per shipment')
        return data

    def create(self, data, *args, **kwargs):
        order_id = data.pop('public_id')
        obj = super().create(data)
        o = Order.objects.get(pk=order_id['id'])
        obj.public_id = o
        obj.save()
        return obj
