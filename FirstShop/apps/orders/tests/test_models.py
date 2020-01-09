from django.test import TestCase
from apps.orders.models import Order, OrderItem
from FirstShop.defs import PaymentOrder, StatusOrder
from datetime import datetime
from django.contrib.auth.models import User


class OrderTest(TestCase):

    def create_order(self):

        my_user = User.objects.create(username='Testuser')

        first_order = Order.objects.create(user=my_user,
                                 public_id=3,
                                 phone='+380671667043',
                                 email='vovchak@gmail.com',
                                 payment=PaymentOrder.PAYOFCARD,
                                 status=StatusOrder.PAID,
                                 date_of_order=datetime.now(),
                                 date_of_paid=datetime.now())

        return first_order

    def test_create_order(self):
        order = self.create_order()
        self.assertTrue(isinstance(order, Order))

class OrderitemTest(TestCase):

    def create_order_item(self):

        my_user = User.objects.create(username='Testuser')

        order_for_connection = Order.objects.create(user=my_user,
                                 public_id=3,
                                 phone='+380671667043',
                                 email='vovchak@gmail.com',
                                 payment=PaymentOrder.PAYOFCARD,
                                 status=StatusOrder.PAID,
                                 date_of_order=datetime.now(),
                                 date_of_paid=datetime.now())

        order_item = OrderItem.objects.create(
            order=order_for_connection,
            product=None,
            amount=33,
            price=999,
            discount=30


        )

        return order_item

    def test_create_order_item(self):
        orderitem = self.create_order_item()
        self.assertTrue(isinstance(orderitem, OrderItem))

