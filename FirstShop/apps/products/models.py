from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length = 200)
    product_price = models.FloatField(default = 0)
    product_avaliable_count = models.PositiveIntegerField(default = 0, null = True)
    product_detail = models.TextField(default = "", editable = True)
    product_can_be_sold = models.BooleanField(default = True)
    product_created_updated = models.DateTimeField(auto_now_add = True)
    product_autor = models.CharField(max_length=200, default=None, null=True)
    publishing_house = models.CharField(max_length=200, default=None, null=True)
    Publication_date = models.CharField(max_length=200, default=None, null=True)
    Number_of_pages = models.IntegerField(default=0)
    def __str__(self):
        return self.product_name
