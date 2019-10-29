from django.db import models
from django.utils import timezone


# from apps.orders.models import Payment

# from apps.orders.models import Order


class Shipment(models.Model):
    pub_order_id = models.CharField(max_length=20)
    # FIXME: enable foreign key after order impl
    # order = models.ForeignKey(
    #    'Order',
    #    on_delete=models.CASCADE,
    # )
    # FIXME: enable foreign key after payment impl
    # is_paid = models.ForeignKey(
    #   'Payment',
    #   on_delete=models.CASCADE
    # )

    # Choice field for delivery service or pickup

    NovaPoshta = 'NP'
    Justin = 'JT'
    Pickup = 'CP'
    DELIVERY = [
        (NovaPoshta, 'Нова Пошта'),
        (Justin, 'Justin'),
        (Pickup, 'Самовывоз')
    ]
    shipment_method = models.CharField(
        max_length=2,
        choices=DELIVERY,
        default=Pickup
    )

    # Choice field for payment method

    PaymentOnDelivery = 'POD'
    InstantPayment = 'INP'
    CardToCard = 'CTC'
    Certificate = 'CTF'

    PAYMENT_METHOD = [
        (PaymentOnDelivery, 'Payment on delivery'),
        (InstantPayment, 'Instant Payment'),
        (CardToCard, 'Card to Card payment'),
        (Certificate, 'Certificate payment')
    ]
    payment_method = models.CharField(
        max_length=3,
        choices=PAYMENT_METHOD,
        default=InstantPayment
    )

    delivery_address = models.CharField(max_length=200)

    # Shipment status field
    shipment_status = models.IntegerField(default=1)
    shipment_status_date = models.DateTimeField('status_date', default=timezone.now)

    def __str__(self):
        return self.pub_order_id
