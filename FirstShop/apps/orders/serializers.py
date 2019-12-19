from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    product_name = serializers.CharField(read_only=True)
    product_price = serializers.CharField(read_only=True)
    product_avaliable_count = serializers.CharField(read_only=True)
    product_detail = serializers.CharField(read_only=True)
    product_can_be_sold = serializers.CharField(read_only=True)
    Publication_date = serializers.CharField(read_only=True)
    Number_of_pages = serializers.CharField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_price', 'product_avaliable_count', 'product_detail',
                  'product_can_be_sold', 'Publication_date', 'Number_of_pages']


class OrderItemSerializer(serializers.ModelSerializer):
    #product = ProductSerializer(many=True, read_only=True)
    product_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['id', 'amount', 'price', 'discount', 'product_id'] #'product',




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
        "id": 86,
        "user": 1,
        "public_id": "1",
        "phone": "3323",
        "email": "q@mai.ru",
        "payment": "PP",
        "status": "PAID",
        "items": [
            {
                "id": 44,
                "order": 86,
                "amount": 1,
                "price": "9999.00",
                "discount": 99,
                "product": [{"id": 1}]
            }
        ]
    }

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
"""
