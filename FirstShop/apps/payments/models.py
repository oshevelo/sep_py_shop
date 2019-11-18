from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpRequest, request
from apps.products.models import Product
# Create your models here.

PAY_PROVIDER = [
    ['Visa', 'Visa'],
    ['MasterCard', 'MasterCard']
]

STATUS = [
    ['In process', 'In process'],
    ['Ready', 'Ready']
]


class BillingLogs(models.Model):
    payment_date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    status = models.CharField(max_length=100, choices=STATUS)
    if request == 'POST':
        info = HttpRequest.POST
    else:
        info = HttpRequest.body


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    payment_id = models.CharField(max_length=100, null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=6, null=True, blank=False)
    date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    provider = models.CharField(max_length=100, choices=PAY_PROVIDER, null=True, blank=False)

    def __str__(self):
        return 'user = {}, payment_id = {}'.format(self.user, self.payment_id, self.pk)
