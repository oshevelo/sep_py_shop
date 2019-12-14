from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from apps.shipments.models import Shipment
from apps.orders.models import Order
from datetime import datetime
from FirstShop.defs import DeliveryStatus, StatusOrder
import random


class ShipmentTestAPI(TestCase):
    def setUp(self):
        """Create 10 orders"""
        for i in range(1, 10):
            Order.objects.create(user='admin',
                                 public_id=1,
                                 phobe='+380634338963',
                                 email='johnny@cash.com',
                                 payment=PaymentOrder.PAYOFCARD,
                                 status=StatusOrder.PAID,
                                 date_of_order=datetime.now(),
                                 date_of_paid=datetime.now()
                                 )
        """Add shipments to orders"""
        for i in range(1, 10):
            Shipment.objects.create(public_id=i,
                                    shipment_provider='Nova Poshta',
                                    delivery_address='Kyiv, Draizera, 4',
                                    post_branch=str(random.randint(1000, 9999)),
                                    shipment_status_date=datetime.now(),
                                    status_change_date=datetime.now(),
                                    shipment_status=DeliveryStatus.WaitForSender
                                    )

        self.c = APIClient()
        print(Shipment.objects.all())

    def test_list(self):
        c = Client()
        response = self.c.get('/shipments/')
        print(response.data)
        print(response.status_code)




