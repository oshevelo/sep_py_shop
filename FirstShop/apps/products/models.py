from django.db import models


class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatField(default = 0)
    avaliable_count = models.PositiveIntegerField(default = 0, null = True)
    detail = models.TextField(default = "", editable = True)
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    #author= models.ForeignKey('Author', on_delete=models.SET_NULL, null = True)
    #gengre = models.ManyToManyField('Gengre')
    #publishing_house = models.ForeignKey(Publishing_house, on_delete=models.SET_NULL, null = True) 
    publication_date = models.DateTimeField()
    number_of_pages = models.IntegerField(default = 0)
    
    
    def  __str__(self):
        return self.name
class Complect(models.Model): 
    name = models.CharField(max_length = 200)
    detail = models.TextField(default = "", editable = True)
    discount = models.DecimalField(default = 0, max_digits=2, decimal_places = 2, null=True, blank=True)
    products = models.ManyToManyField(Product)
    def __str__(self):
        return self.name
        