from django.contrib import admin
from .models import Provider


class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_id',
        'delivery_address',
        'post_branch',
        'shipment_status',
        'shipment_status_date'
    )


admin.site.register(Provider, ProviderAdmin)
