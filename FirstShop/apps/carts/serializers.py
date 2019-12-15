from rest_framework import  serializers
from apps.carts.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'price', 'discount', 'amount', 
        'cart_item_create', 'cart_item_update']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        cartitem = CartItem.objects.create(**validated_data)
        for items_data in items_data:
            Cart.objects.create(cartitem=cartitem, **items_data)
        return cartitem


class CartSerializer(serializers.ModelSerializer):

    items = CartItemSerializer(many=True)


    class Meta:
        model = Cart
        fields = ['user', 'public_id', 'cart_create', 'cart_update', 'items']
