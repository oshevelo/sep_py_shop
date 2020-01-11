from django.db import models
import os
from django.contrib.postgres.fields import JSONField
from PIL import Image
import uuid

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatField(default = 0)
    avaliable_count = models.PositiveIntegerField(default = 0, null = True)
    detail = models.TextField(default = "", editable = True)
    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    attributes = JSONField(default = '')
    
    def  __str__(self):
        return self.name

class Gallery(models.Model):
    
    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "{}.{}".format(uuid.uuid4(), extension)
        return os.path.join("images", filename)

    def save(self):
        super(Gallery, self).save()
        picture = Image.open(self.photo)
        sizes = [
            (128,128),  #small
            (310,350),  #medium   
            (400,450),  #big
        ]
        for size in sizes:
            resized_picture = picture.resize(size)
            resized_picture.save(self.photo.path[:-4] + str(size), format = 'PNG')

    photo = models.ImageField(verbose_name='photo' , upload_to= get_file_path, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True, related_name = 'photos')

class Complect(models.Model): 
    name = models.CharField(max_length = 200)
    detail = models.TextField(default = "", editable = True)
    discount = models.DecimalField(default = 0, max_digits=2, decimal_places = 2, null=True, blank=True)
    products = models.ManyToManyField(Product)
    def __str__(self):
        return self.name
        