from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length = 200)
    product_price = models.FloatField(default = 0)
    product_avaliable_count = models.PositiveIntegerField(default = 0, null = True)
    product_detail = models.TextField(default = "", editable = True)
    product_can_be_sold = models.BooleanField(default = True)
    product_created_updated = models.DateTimeField(auto_now_add = True)
    #author_name= models.ForeignKey(Author, on_delete=models.SET_NULL, null = True)
    #gengre = models.ManyToManyField(Gengre)
    #publishing_house = models.ForeignKey(Publishing_house, on_delete=models.SET_NULL, null = True) 
    Publication_date = models.DateTimeField()
    Number_of_pages = models.IntegerField(default = 0)
    def __str__(self):
        return self.product_name
