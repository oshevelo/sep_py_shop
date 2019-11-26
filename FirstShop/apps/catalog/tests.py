from django.test import TestCase

from django.test import Client


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        pass
        # Issue a GET request.
        response = self.client.get('/catalog/categories/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
