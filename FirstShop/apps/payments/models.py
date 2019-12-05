from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from apps.products.models import Product
from django.contrib.postgres.fields import JSONField
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    payment_date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    status = models.CharField(max_length=100, choices=STATUS, null=True, blank=False)
    data = JSONField(null=True, blank=False)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=True, blank=False)
    date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    provider = models.CharField(max_length=100, choices=PAY_PROVIDER, null=True, blank=False)

    def __str__(self):
        return 'user = {}, id = {}, date = {}'.format(self.user, self.id, self.date, self.pk)

