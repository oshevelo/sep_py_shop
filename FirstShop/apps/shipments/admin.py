from django.contrib import admin
from .models import Shipment, ShipmentLog


class ShipmentAdmin(admin.ModelAdmin):
    list_display = (
        'public_id',
        'shipment_provider',
        'delivery_address_city',
        'delivery_address_area',
        'delivery_address_area_region',
        'delivery_address_street',
        'delivery_address_house',
        'delivery_address_flat',
        'shipment_status',
        'shipment_status_date'
    )

class ShipmentLogAdmin(admin.ModelAdmin):
    list_display = (
        'public_id',
        'send_date',
        'log_field',
        'request',
        'response_status'
    )


admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(ShipmentLog, ShipmentLogAdmin)
