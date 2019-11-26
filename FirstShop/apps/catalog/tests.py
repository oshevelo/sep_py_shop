from django.test import TestCase


class SimpleTest(TestCase):

    def test_details(self):
        pass
        # Issue a GET request.
        response = self.client.get('/catalog/categories/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
