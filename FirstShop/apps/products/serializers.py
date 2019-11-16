from rest_framework.serializers import ModelSerializer
from .models import Book
class BookSerializer(ModelSerializer):
	class Meta:
		model = Book
		fields = (
		'book_name', 
		'book_price',
		'book_avaliable_count',
		'book_detail',
		'book_can_be_sold',
		'book_created_updated',
		#'author_name',
		#'gengre',
		#'publishing_house',
		'Publication_date', 
		'Number_of_pages'
		)
