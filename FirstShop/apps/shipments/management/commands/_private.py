from apps.shipments.models import ShipmentLog
from django.utils import timezone


def save_log(params, response):
    delivery_api_log = ShipmentLog()
    delivery_api_log.send_date = timezone.now()
    delivery_api_log.log_field = response.text
    delivery_api_log.request = params
    delivery_api_log.response_status = response.status_code
    delivery_api_log.save()