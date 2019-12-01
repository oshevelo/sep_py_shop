from rest_framework.serializers import ModelSerializer
from .models import Product,  Complect
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
        'id',
        'name', 
        'price',
        'avaliable_count',
        'detail',
        'can_be_sold',
        'created',
        'updated',
        #'author',
        #'gengre',
        #'publishing_house',
        'publication_date', 
        'number_of_pages',
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