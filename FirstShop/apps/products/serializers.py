from rest_framework.serializers import ModelSerializer
from .models import Product
class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product
		fields = (
		'id',
		'product_name', 
		'product_price',
		'product_avaliable_count',
		'product_detail',
		'product_can_be_sold',
		'product_created_updated',
		#'author_name',
		#'gengre',
		#'publishing_house',
		'Publication_date', 
		'Number_of_pages',
		)
