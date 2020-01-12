from rest_framework.serializers import ModelSerializer
from .models import Product, Complect
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
        'id',
        'name', 
        'price',
        'avaliable_count',
        'detail',
        'active',
        'created',
        'updated',
        'attributes',
        )
class ComplectSerializer(ModelSerializer):
    class Meta:
        model = Complect
        fields = (
        'id'
        'name',
        'detail',
        'discount',
        'products',
        )