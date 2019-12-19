from django.db import models
from django.contrib.postgres.fields import JSONField
from apps.orders.models import Order #,  Payment
from FirstShop.defs import DeliveryStatus, DeliveryProvider

# from FirstShop.apps.orders.models import Payment


class Shipment(models.Model):

    public_id = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='my_shipment',
        null=True,
        default=None
    )

    DELIVERY = [
        (DeliveryProvider.novaposhta, 'Nova Poshta'),
        (DeliveryProvider.justin, 'Justin'),
        (DeliveryProvider.pickup, 'Pickup')
    ]

    shipment_provider = models.CharField(
        max_length=20,
        choices=DELIVERY,
        default=DeliveryProvider.pickup
    )

    delivery_address_city = models.CharField(
        max_length=100,
        default=None,
        null=True
    )
    delivery_address_area = models.CharField(
        max_length=100,
        default=None,
        null=True
    )
    delivery_address_area_region = models.CharField(
        max_length=100,
        default=None,
        null=True
    )
    delivery_address_street = models.CharField(
        max_length=100,
        default=None,
        null=True
    )
    delivery_address_house = models.CharField(
        max_length=100,
        default=None,
        null=True
    )
    delivery_address_flat = models.CharField(
        max_length=100,
        default=None,
        null=True
    )

    post_branch = models.CharField(
        max_length=200,
        default=None,
        null=True
    )
    shipment_status_date = models.DateTimeField(
        'status_date',
        auto_now=True
    )
    status_change_date = models.DateTimeField(
        'status_date_change',
        auto_created=True
    )

    shipment_status = models.IntegerField(
        default=DeliveryStatus.WaitForSender,
        choices=DeliveryStatus.DELIVERY_STATUS
    )

    invoice_id = models.CharField(
        max_length=200,
        null=True,
        default=None,
        verbose_name='Document Number'
    )

    class Meta:
        app_label = 'shipments'
        ordering = ['public_id']

    def __str__(self):
        return 'order {}'.format(self.invoice_id)


class ShipmentLog(models.Model):
    public_id = models.OneToOneField(
        Shipment,
        on_delete=models.CASCADE,
        related_name='my_shipment_log',
        blank=True,
        null=True
    )

    send_date = models.DateTimeField(
        verbose_name='Send Date',
        auto_now_add=True
    )

    log_field = models.TextField(
        verbose_name='Log',
        blank=True,
        null=True   
    )

    request = models.TextField(
        verbose_name='Request',
        blank=True,
        null=True
    )

    response_status = models.CharField(
        max_length=100,
        default=None,
        null=True
    )
