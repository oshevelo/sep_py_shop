from django.db import models
#from apps.orders.models import Order


class Shipment(models.Model):
    pub_order_id = models.CharField()
    #FIXME: enable foreign key after order impl
    #order = models.ForeignKey(
    #    'Order',
    #    on_delete=models.CASCADE,
    #)
    
