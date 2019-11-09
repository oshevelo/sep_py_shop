from django.contrib import admin

from .models import Product
from .models import ProductStatistics


admin.site.register(Product)
admin.site.register(ProductStatistics)

