
from apps.orders.models import Order, OrderItem
from apps.shipments.models import ShipmentLog, Shipment
from django.utils import timezone
import requests
import datetime


def create_delivery(order_id):
    try:
        int(order_id)
    except ValueError:
        print("Wrong order id type")
    else:
        check_order = Order.objects.filter(pk=order_id).first()
        if not check_order:
            print("Order is not exist")
        else:
            params = {
                    "invoice_id": Shipment.objects.values_list('invoice_id', flat=True).get(public_id=order_id),
                    "delivery_address": Shipment.objects.values_list('delivery_address', flat=True).get(
                        public_id=order_id),
                    "user_name": Order.objects.values_list('user', flat=True).get(
                        public_id=order_id),
                    "post_branch": Shipment.objects.values_list('delivery_address', flat=True).get(public_id=order_id),
                    "status_change_date": str(datetime.datetime.now()),
                    "shipment_status": Shipment.objects.values_list('shipment_status', flat=True).get(
                        public_id=order_id)
                }

    response = requests.post('http://localhost:8000/delivery_api/', json=params, headers={'format': 'json'}).text

    delivery_api_log = ShipmentLog()
    delivery_api_log.send_date = timezone.now()
    delivery_api_log.log_field = response
    delivery_api_log.request = params
    if response:
        delivery_api_log.is_processed = True
    else:
        delivery_api_log.is_processed = False
    delivery_api_log.save()

    return response


def handle(order_id):
    order_id = input("Input order document number: ")
    params = {
        "OrderID": order_id,
    }
    try:
        int(order_id)
    except ValueError:
        print("Wrong order id type")
    else:
        response = requests.get('http://localhost:8000/delivery_api/'+order_id, headers={'format': 'json'}).text
        delivery_api_log = ShipmentLog()
        delivery_api_log.send_date = timezone.now()
        delivery_api_log.log_field = response
        delivery_api_log.request = params
        if response:
            delivery_api_log.is_processed = True
        else:
            delivery_api_log.is_processed = False
        delivery_api_log.save()

    return response

