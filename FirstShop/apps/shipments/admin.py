from django.contrib import admin
from .models import Shipment


class ShipmentInLine(admin.TabularInline):
    model = Shipment
    extra = 5


class ShipmentAdmin(admin.ModelAdmin):

    list_display = ('pub_order_id', 'shipment_method', 'payment_method', 'delivery_address', 'shipment_status', 'shipment_status_date')


admin.site.register(Shipment, ShipmentAdmin)


