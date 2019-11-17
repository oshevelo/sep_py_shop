# class Payment to orders



class PaymentOrder:

    CASH = 'CA'
    CREDIT = 'CR'
    PRIVATPAY = 'PP'
    PAYOFPARTS = 'POP'
    PAYOFCARD = 'POC'


    PAYMENT_CHOICES =[
        (CASH, 'Cash'),
        (CREDIT, 'Credit'),
        (PRIVATPAY, 'PrivatPay'),
        (PAYOFPARTS, 'Pay of parts'),
        (PAYOFCARD, 'Pay of card'),
    ]


class StatusOrder:

    ACCEPTED_FOR_PROCESSING = 'AFP'
    PROCESSING = 'PR'
    PAID = 'PA'
    DONE = 'DO'


    STATUS_CHOICES = [
        ('ACCEPTED_FOR_PROCESSING', 'Accepted for processing'),
        ('PROCESSING', 'Processing'),
        ('PAID', 'Paid'),
        ('DONE', 'Done'),
]
