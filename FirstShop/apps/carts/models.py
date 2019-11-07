from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


PROVIDER_CHOICES = [
    ('Rozetka', 'Rozetka'),
    ('Буква', 'Буква'),
    ('Globalbook', 'Globalbook'),
    ('Букля', 'Букля'),
    ('Yakaboo', 'Yakaboo')
]


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    public_id = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'user = {}, public_id = {}'.format(self.user, self.public_id, self.pk)


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    #product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    discount = models.PositiveIntegerField(default=None, null=True, blank=True)
    #recs = models.ForeignKey(Recommendation, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveIntegerField(default=1, null=True, blank=False)
    provider = models.CharField(max_length=100, choices=PROVIDER_CHOICES, null=True, blank=False)

    def __str__(self):
        return '{}'.format(self.cart_id)
