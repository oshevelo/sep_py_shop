from django.db import models
from FirstShop.defs import DeliveryStatus


class Provider(models.Model):

    invoice_id = models.CharField(
        max_length=200,
        null=True,
        default=None,
        verbose_name='DocumentNumber'
    )
    user_name = models.CharField(
        max_length=200,
        null=True,
        default=None,
    )

    delivery_address = models.CharField(
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

    class Meta:
        app_label = 'delivery_api'

    def __str__(self):
        return 'Invoice '.format(self.invoice_id)

