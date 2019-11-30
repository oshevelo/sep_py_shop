from django.test import TestCase
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site

class BaseAcceptanceTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

class AdminTest(BaseAcceptanceTest):

class PostViewTest(BaseAcceptanceTest):

