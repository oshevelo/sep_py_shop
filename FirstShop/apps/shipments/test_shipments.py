from django.test import TestCase
from rest_framework import status
from django.utils import timezone
from rest_framework.test import APIClient
from apps.shipments.models import Shipment
from apps.orders.models import Order
from FirstShop.defs import DeliveryStatus, StatusOrder
import random
from FirstShop.defs import *


class ShipmentTestAPI(TestCase):
    def setUp(self):
        """Create 10 orders"""
        for i in range(1, 10):
            Order.objects.create(#user=Order.objects.get(user=i),
                                 public_id=i,
                                 phone='+380634338963',
                                 email='johnny@cash.com',
                                 payment=PaymentOrder.PAYOFCARD,
                                 status=StatusOrder.PAID,
                                 date_of_order=timezone.now(),
                                 date_of_paid=timezone.now()
                                 )
        """Add shipments to orders"""
        for i in range(1, 10):
            Shipment.objects.create(public_id=Order.objects.get(public_id=i),
                                    shipment_provider='Nova Poshta',
                                    delivery_address_city='Kyiv',
                                    delivery_address_area='',
                                    delivery_address_area_region='',
                                    delivery_address_street='Kurnatovskoho',
                                    delivery_address_house='19A',
                                    delivery_address_flat='78',
                                    post_branch=str(random.randint(1000, 9999)),
                                    shipment_status_date=timezone.now(),
                                    status_change_date=timezone.now(),
                                    shipment_status=DeliveryStatus.WaitForSender
                                    )

        self.c = APIClient()
        print(Shipment.objects.all())

    def test_list(self):
        c = APIClient()
        response = self.c.get('/shipments/')
        print(response.data)
        print(response.status_code)