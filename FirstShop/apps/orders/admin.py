from django.contrib import admin
from .models import Order, OrderItem



class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'public_id',
        'user',
        'delivery',
        'payment',
        'status',
        'date'
    )

class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        #'product_id',
        'amount',
        'price',
        'discount',

    )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
