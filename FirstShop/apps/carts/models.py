from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from apps.products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    public_id = models.CharField(max_length=200, blank=False)
    cart_create = models.DateTimeField(null=True, blank=True)
    cart_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return 'user = {}, public_id = {}, pk = {}'.format(self.user, self.public_id, self.pk)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True)
    discount = models.PositiveIntegerField(default=None, null=True, blank=True)
    amount = models.PositiveIntegerField(default=1, null=True, blank=False)
    cart_item_create = models.DateTimeField(null=True, blank=True)
    cart_item_update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.cart)
