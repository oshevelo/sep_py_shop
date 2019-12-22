# class Payment to orders


class PaymentOrder:

    CASH = 'CASH'
    CREDIT = 'CREDIT'
    PRIVATPAY = 'PRIVAT_PAY'
    PAYOFPARTS = 'PAY_OF_PARTS'
    PAYOFCARD = 'PAY_OF_CARD'


    PAYMENT_CHOICES =[
        (CASH, 'Cash'),
        (CREDIT, 'Credit'),
        (PRIVATPAY, 'PrivatPay'),
        (PAYOFPARTS, 'Pay of parts'),
        (PAYOFCARD, 'Pay of card'),
    ]

class DeliveryStatus:
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

    delivery_address = 'Kyiv'
    post_branch = '0001'
    shipment_status_date = '01.01.2020'

    DELIVERY_STATUS = [
        (WaitForSender, 'Нова пошта очікує надходження від відправника'),
        (DeletedForm, 'Видалено'),
        (NumberNotFound, 'Номер не знайдено'),
        (DeliveryInOblast, f'Відправлення у місті {delivery_address}'),
        (DeliveryInLocal, f'Відправлення у місті {delivery_address}'),
        (DeliveryOnTheWay, 'Відправлення прямує до міста'),
        (DeliveryInTheCity,
         f'Відправлення у місті {delivery_address}, орієнтовна доставка до ВІДДІЛЕННЯ-{post_branch} Очікуйте додаткове повідомлення про прибуття.'),
        (DeliveryOnTheBranch_1, 'Прибув на відділення'),
        (DeliveryOnTheBranch_2, 'Прибув на відділення'),
        (DeliveryReceived, 'Відправлення отримано'),
        (DeliveryReceivedCashback,
         f'Відправлення отримано {shipment_status_date}. Протягом доби ви одержите SMS-повідомлення про надходження грошового переказу та зможете отримати його в касі відділення «Нова пошта»'),
        (DeliveryReceivedCashbackGet, f'Відправлення отримано {shipment_status_date}. Грошовий переказ видано одержувачу.'),
        (DeliveryReceivedCheck, 'Відправлення передано до огляду отримувачу'),
        (OnTheWayToCustomer, 'На шляху до одержувача'),
        (RejectBySender_1, 'Відмова одержувача'),
        (RejectBySender_2, 'Відмова одержувача'),
        (RejectBySender_3, 'Відмова одержувача'),
        (DeliveryAddressChange, 'Змінено адресу'),
        (DeliveryHoldEnd, 'Припинено зберігання'),
        (DeliveryBack, 'Одержано і створено ЄН зворотньої доставки')
    ]


class DeliveryProvider(object):
    novaposhta = 'Nova Poshta'
    justin = 'Justin'
    pickup = 'Pickup'


class StatusOrder:

    ACCEPTED_FOR_PROCESSING = 'ACCEPTED_FOR_PROCESSING'
    PROCESSING = 'PROCESSING'
    PAID = 'PAID'
    DONE = 'DONE'


    STATUS_CHOICES = [
        (ACCEPTED_FOR_PROCESSING, 'Accepted for processing'),
        (PROCESSING, 'Processing'),
        (PAID, 'Paid'),
        (DONE, 'Done'),
]
