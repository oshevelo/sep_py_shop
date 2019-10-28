from django.db import models


# from apps.orders.models import Order


class Shipment(models.Model):
    pub_order_id = models.CharField()
    # FIXME: enable foreign key after order impl
    # order = models.ForeignKey(
    #    'Order',
    #    on_delete=models.CASCADE,
    # )

    # Choose delivery service or pickup

    NovaPoshta = 'NP'
    Justin = 'JT'
    Pickup = 'CP'
    DELIVERY = [
        (NovaPoshta, 'Нова Пошта'),
        (Justin, 'Justin'),
        (Pickup, 'Самовывоз')
    ]
    shipment_method = models.CharField(max_length=2, choices=DELIVERY, default=Pickup)

    # Choose field for payment method

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
    payment_method = models.CharField(max_length=3, choices=PAYMENT_METHOD, default=InstantPayment)

    delivery_address = models.CharField()
