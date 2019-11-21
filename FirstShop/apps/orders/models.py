from FirstShop.defs import PaymentOrder, StatusOrder

from django.db import models
from django.contrib.auth.models import User

# from apps.product.models. import Product

# from apps.orders.models import Payment

from django.utils import timezone

ORDERS_STATUS_CHOICES = [
    ('Accepted_for_processing', 'Accepted for processing'),
    ('Processing', 'Processing'),
    ('Paid', 'Paid'),
]

PAYMENT_CHOICES =[
    ('Cash', 'Cash'),
    ('Credit', 'Credit'),
    ('PrivarPay', 'PrivarPay'),
    ('Pay_of_parts', 'Pay of parts'),
    ('Pay_of_card', 'Pay of card'),
]


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    public_id = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)

    payment = models.CharField(max_length=100, choices=PaymentOrder.PAYMENT_CHOICES,
                               default=PaymentOrder.CREDIT, null=True, blank=False)
    status = models.CharField(max_length=100, choices=StatusOrder.STATUS_CHOICES,
                              default=StatusOrder.ACCEPTED_FOR_PROCESSING, null=True, blank=False)
    date_of_order = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_of_paid = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return 'user = {}, status = {}, id = {},'.format(self.user, self.status, self.pk,)

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    # product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveIntegerField(default=1, null=True, blank=False)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=False)
    discount = models.PositiveIntegerField(default=None, null=True, blank=True)

    def __str__(self):
        return '{}, price = {}'.format(self.order, self.price)
