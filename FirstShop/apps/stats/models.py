from django.db import models

import datetime
from django.utils import timezone


from django.db import models


class Product(models.Model):
	class Meta:
		db_table = "product"
	
	product_name = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.product_name


class ProductStatistics(models.Model):
	class Meta:
    db_table = "productStats"
     
	product = models.ForeignKey(Product, on_delete = models.PROTECT)                  
	date = models.DateField('Date', default=timezone.now)
	views = models.IntegerField('Views', default=0)
     
	def __str__(self):
		return self.product.product_name
     
