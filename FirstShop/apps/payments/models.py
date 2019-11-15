from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=6)
    date = models.DateTimeField(default=timezone.now)
