from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.products.serializers import ProductSerializer



class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['id', 'amount', 'price', 'discount', 'product_id', 'product']




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




#default_read_only=TRUE
#default_read_only=False


""""" NOTES
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



""""

{
    "user": 1,
    "public_id": "1",
    "phone": "3323",
    "email": "q@mai.ru",
    "payment": "PP",
    "status": "PAID",
    "items": [
        {
            "amount": 1,
            "price": "9999.00",
            "discount": 99,
            "product_id": 2
        }
    ]
}

{
    "id": 11,
    "user": 1,
    "public_id": "1",
    "phone": "8888888",
    "email": "q@mai.ru",
    "payment": "PP",
    "status": "PAID",
    "items": [
        {
            "id": 11,
            "amount": 1,
            "price": "9999.00",
            "discount": 99,
            "product_id": 3,
            "product": {
                "id": 3,
                "name": "pepsi",
                "price": "456.0",
                "avaliable_count": "89",
                "detail": "very many",
                "active": "True",
                "created": "2019-12-20 18:01:37.059589+00:00",
                "updated": "2019-12-20 18:01:37.059618+00:00",
                "publication_date": "2019-12-20 20:01:00+00:00",
                "number_of_pages": "3"
            }
        }
    ]
}

"""
