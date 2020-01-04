from rest_framework import  serializers
from apps.carts.models import Cart, CartItem
from apps.products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['cart', 'price', 'discount', 'amount', 'product']


class CartSerializer(serializers.ModelSerializer):

    items = CartItemSerializer(many=True)


    class Meta:
        model = Cart
        fields = ['user', 'public_id', 'cart_create', 'cart_update', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        cart = Cart.objects.create(**validated_data)
        for items_data in items_data:
            CartItem.objects.create(cart=cart, **items_data)
        return cart