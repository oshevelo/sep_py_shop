from django.contrib import admin

from .models import Product
from .models import ProductStatistics
from .models import UserStatistics


admin.site.register(Product)
admin.site.register(ProductStatistics)
admin.site.register(UserStatistics)


