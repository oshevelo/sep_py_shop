from rest_framework import serializers
from apps.orders.models import Order, OrderItem



class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'amount', 'price', 'discount', 'product_id']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)


    class Meta:
         model = Order  # THIS IS Order!
         fields = ['id', 'user', 'public_id', 'phone', 'email', 'payment', 'status', 'items']


    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order



""""" NOTES
    def create(self, validated_data):                       #спитати за цю штуку щоб посилатися на одного?
        item_id = validated_data.pop('items')               # яка різниця між цими create -тами
        obj = super().create(**validated_data)
        item = OrderItem.objects.get(item_id['id'])
        obj.items = item
        obj.save()
        return obj
        

    def create(self,data, *args, **kwargs):
        items_id = data.pop('items')         # THIS ARRAY ITEMS FROM OBJECTS
        obj = super().create(data)                 # THIS IS Order!
        o = Order.objects.get(pk=items_id['id'])
        obj.items = o
        obj.save()
        return obj


    # It is second version realisation:
    def get_fields(self):
        fields = super(OrderSerializer, self).get_fields()
        fields['items'] = OrderItemSerializer(many=True)
        return fields

    #######Sample it for me
    # sub_category = CategorySerializer(many=True)
    # top_category = TopCategorySerializer()
    #######
    # фільтер нам дає зажди масив, filter())
    #first завжди повертає 1 елемент з цього масива )
    # це щоб на один заказ не можна було привязати дві доставки

"""""





