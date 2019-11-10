from django.contrib import admin
from .models import BaseShipment


class ShipmentInLine(admin.TabularInline):
    model = BaseShipment
    extra = 5


class ShipmentAdmin(admin.ModelAdmin):
    list_display = (
        'public_order',
        'shipment_provider',
        # 'payment_method',
        # FIXME: add if it needed
        'delivery_address',
        'shipment_status',
        'shipment_status_date'
    )


admin.site.register(BaseShipment, ShipmentAdmin)
