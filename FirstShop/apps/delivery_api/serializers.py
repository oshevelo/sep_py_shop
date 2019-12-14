from rest_framework import serializers
from apps.delivery_api.models import Provider


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = (
            'invoice_id',
            'delivery_address',
            'user_name',
            'post_branch',
            'shipment_status_date',
            'status_change_date',
            'shipment_status'
        )
