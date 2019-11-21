from rest_framework import serializers
from apps.orders.models import Order, OrderItem



class OrderItemSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField()
    amount = serializers.IntegerField(min_value=0, default=1)
    price = serializers.DecimalField(max_digits=100, decimal_places=2, default=11)
    discount = serializers.IntegerField(max_value=100, min_value=0, default=0)

    class Meta:
        model = OrderItem
        fields = ('id', 'amount', 'price', 'discount')



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    id = serializers.IntegerField()

    class Meta:
         model = Order
         fields = ('id', 'user', 'public_id', 'phone', 'email', 'payment', 'status', 'items')



    def create(self,data, *args, **kwargs):
        items_id = data.pop('items')
        obj = super().create(data)
        o = Order.objects.get(pk=items_id['id'])
        obj.items = o
        obj.save()
        return obj





    # це другий спосіб реалізації
    # def get_fields(self):
    #     fields = super(OrderSerializer, self).get_fields()
    #     fields['items'] = OrderItemSerializer(many=True)
    #
    #     return fields









