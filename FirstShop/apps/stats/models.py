from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import Userimport JSONField

'''
class Product(models.Model):
	class Meta:
		db_table = "product"
	
	product_name = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.product_name


class ProductStatistics(models.Model):
	class Meta:
        	db_table = "statistics"
     
	product = models.ForeignKey(Product, on_delete = models.PROTECT)                  
	date = models.DateField('Date', default=timezone.now)
	views = models.IntegerField('Views', default=0)
     
	def __str__(self):
		return self.product.product_name
'''

class Statistics(models.Model):
	class Meta:
        	db_table = "statistics"
     
	user = models.ForeignKey(User, on_delete = models.PROTECT)                  
	date = models.DateField('Date', default=timezone.now)
	session = models.DurationField('Session', default=0)
	source = models.CharField(max_length = 200)
	data = JSONField()
     
	def __str__(self):
		return self.user
     


