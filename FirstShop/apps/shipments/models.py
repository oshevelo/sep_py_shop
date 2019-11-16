from django.db import models

# from FirstShop.apps.orders.models import Payment
from apps.orders.models import Order
from FirstShop.variables import DeliveryStatus, DeliveryProvider


class BaseShipment(models.Model):

    public_order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name='my_shipment',
        blank=True,
        null=True
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
        auto_now_add=True
    )
    status_change_date = models.DateTimeField(
        'status_change_date',
        auto_now=True
    )

    DELIVERY_STATUS = [
        (DeliveryStatus.WaitForSender, 'Нова пошта очікує надходження від відправника'),
        (DeliveryStatus.DeletedForm, 'Видалено'),
        (DeliveryStatus.NumberNotFound, 'Номер не знайдено'),
        (DeliveryStatus.DeliveryInOblast, f'Відправлення у місті {delivery_address}'),
        (DeliveryStatus.DeliveryInLocal, f'Відправлення у місті {delivery_address}'),
        (DeliveryStatus.DeliveryOnTheWay, 'Відправлення прямує до міста'),
        (DeliveryStatus.DeliveryInTheCity,
         f'Відправлення у місті {delivery_address}, орієнтовна доставка до ВІДДІЛЕННЯ-{post_branch} Очікуйте додаткове повідомлення про прибуття.'),
        (DeliveryStatus.DeliveryOnTheBranch_1, 'Прибув на відділення'),
        (DeliveryStatus.DeliveryOnTheBranch_2, 'Прибув на відділення'),
        (DeliveryStatus.DeliveryReceived, 'Відправлення отримано'),
        (DeliveryStatus.DeliveryReceivedCashback,
         f'Відправлення отримано {shipment_status_date}. Протягом доби ви одержите SMS-повідомлення про надходження грошового переказу та зможете отримати його в касі відділення «Нова пошта»'),
        (DeliveryStatus.DeliveryReceivedCashbackGet, f'Відправлення отримано {shipment_status_date}. Грошовий переказ видано одержувачу.'),
        (DeliveryStatus.DeliveryReceivedCheck, 'Відправлення передано до огляду отримувачу'),
        (DeliveryStatus.OnTheWayToCustomer, 'На шляху до одержувача'),
        (DeliveryStatus.RejectBySender_1, 'Відмова одержувача'),
        (DeliveryStatus.RejectBySender_2, 'Відмова одержувача'),
        (DeliveryStatus.RejectBySender_3, 'Відмова одержувача'),
        (DeliveryStatus.DeliveryAddressChange, 'Змінено адресу'),
        (DeliveryStatus.DeliveryHoldEnd, 'Припинено зберігання'),
        (DeliveryStatus.DeliveryBack, 'Одержано і створено ЄН зворотньої доставки')
    ]

    shipment_status = models.IntegerField(
        default=DeliveryStatus.WaitForSender,
        choices=DELIVERY_STATUS
    )

    invoice_id = models.CharField(
        max_length=200,
        null=True,
        default=None
    )

    class Meta:
        app_label = 'shipments'
        unique_together = ['public_order', 'delivery_address']
        ordering = ['public_order']

    def __str__(self):
        return 'order {}'.format(self.invoice_id)
