from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# from FirstShop.apps.orders.models import Payment

from apps.orders.models import Order, OrderItem

city = 'Kyiv'
branch = 'Branch #1'
DateToReceive = '01-12-2019 12:00:00'
DateReceived = '02-12-2019 12:00:00'
API_Key = 'b313e7c9662a02870c0d1b8a0cb9e683'


class BaseShipment(models.Model):
    pub_order = models.ForeignKey(
        'orders.OrderItem',
        on_delete=models.CASCADE,
    )
    delivery = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
    )
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
    # FIXME: Enable if it needed
    # PaymentOnDelivery = 'POD'
    # InstantPayment = 'INP'
    # CardToCard = 'CTC'
    # Certificate = 'CTF'
    #
    # PAYMENT_METHOD = [
    #     (PaymentOnDelivery, 'Payment on delivery'),
    #     (InstantPayment, 'Instant Payment'),
    #     (CardToCard, 'Card to Card payment'),
    #     (Certificate, 'Certificate payment')
    # ]
    #
    # payment_method = models.CharField(
    #     max_length=3,
    #     choices=PAYMENT_METHOD,
    #     default=InstantPayment
    # )

    delivery_address = models.CharField(max_length=200)

    # Shipment status field

    WaitForSender = 1
    DeletedForm = 2
    NumberNotFound = 3
    DeliveryInOblast = 4
    DeliveryInLocal = 41
    DeliveryOnTheWay = 5
    DeliveryInTheCity = 6
    DeliveryOnTheBranch_1 = 7
    DeliveryOnTheBranch_2 = 8
    DeliveryReceived = 9
    DeliveryReceivedCashback = 10
    DeliveryReceivedCashbackGet = 11
    DeliveryReceivedCheck = 14
    OnTheWayToCustomer = 101
    RejectBySender_1 = 102
    RejectBySender_2 = 103
    RejectBySender_3 = 108
    DeliveryAddressChange = 104
    DeliveryHoldEnd = 105
    DeliveryBack = 106

    DELIVERY_STATUS = [
        (WaitForSender, 'Нова пошта очікує надходження від відправника'),
        (DeletedForm, 'Видалено'),
        (NumberNotFound, 'Номер не знайдено'),
        (DeliveryInOblast, f'Відправлення у місті {city}'),
        (DeliveryInLocal, f'Відправлення у місті {city}'),
        (DeliveryOnTheWay, 'Відправлення прямує до міста'),
        (DeliveryInTheCity,
         f'Відправлення у місті {city}, орієнтовна доставка до ВІДДІЛЕННЯ-{branch} {DateToReceive} Очікуйте додаткове повідомлення про прибуття.'),
        (DeliveryOnTheBranch_1, 'Прибув на відділення'),
        (DeliveryOnTheBranch_2, 'Прибув на відділення'),
        (DeliveryReceived, 'Відправлення отримано'),
        (DeliveryReceivedCashback,
         f'Відправлення отримано {DateReceived}. Протягом доби ви одержите SMS-повідомлення про надходження грошового переказу та зможете отримати його в касі відділення «Нова пошта»'),
        (DeliveryReceivedCashbackGet, f'Відправлення отримано {DateReceived}. Грошовий переказ видано одержувачу.'),
        (DeliveryReceivedCheck, 'Відправлення передано до огляду отримувачу'),
        (OnTheWayToCustomer, 'На шляху до одержувача'),
        (RejectBySender_1, 'Відмова одержувача'),
        (RejectBySender_2, 'Відмова одержувача'),
        (RejectBySender_3, 'Відмова одержувача'),
        (DeliveryAddressChange, 'Змінено адресу'),
        (DeliveryHoldEnd, 'Припинено зберігання'),
        (DeliveryBack, 'Одержано і створено ЄН зворотньої доставки')
    ]

    shipment_status = models.IntegerField(
        default=WaitForSender,
        choices=DELIVERY_STATUS
    )

    shipment_status_date = models.DateTimeField('status_date', default=timezone.now)

    class Meta:
        app_label = 'shipments'

    def __str__(self):
        return f'order = {self.pub_order_id},pu  delivery_address = {self.delivery_address}, status = {self.shipment_status}'

    def track_delivery(self):
        pass

    def delivery_to_branch(self):
        pass

    def delivery_to_address(self):
        pass