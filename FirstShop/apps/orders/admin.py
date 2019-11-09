from django.contrib import admin
from .models import Order, OrderItem



class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'public_id',
        'user',
        'payment',
        'status',

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
