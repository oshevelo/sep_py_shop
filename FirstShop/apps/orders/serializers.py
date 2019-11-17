from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from FirstShop.defs import PaymentOrder, StatusOrder



class OrderSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    user = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    payment = serializers.ChoiceField(choices=PaymentOrder.PAYMENT_CHOICES, default=PaymentOrder.CASH)
    status = serializers.ChoiceField(choices=StatusOrder.STATUS_CHOICES, default=StatusOrder.ACCEPTED_FOR_PROCESSING)

    class Meta:
        model = Order
        fields = ['id', 'user', 'phone', 'email', 'payment', 'status']


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'amount', 'price', 'discount', 'order']

    def create(self, data, *args, **kwargs):
        order_id = data.pop('order')
        obj = super().create(data)
        o = Order.objects.get(pk=order_id['id'])
        obj.public_order = o
        obj.save()
        return obj
