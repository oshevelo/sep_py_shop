from django.contrib import admin
from .models import Product, Complect, Gallery 
class ImageInline(admin.StackedInline):
    model = Gallery
class MyObjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
admin.site.register(Product,MyObjectAdmin)
admin.site.register(Complect)
admin.site.register(Gallery)