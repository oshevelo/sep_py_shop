import json

from django.test import TestCase
from django.test import tag
from apps.catalog.models import Category


class SimpleTest(TestCase):

    def setUp(self):
        top_category = Category.objects.create(category_name='test_top_category')
        Category.objects.create(category_name='test_sub_category', top_category=top_category)

    # @tag('smoke')
    # def test_get_list_smoke(self):
    #     response = self.client.get('/catalog/categories/')
    #
    #     self.assertContains(response, "test_top_category", status_code=200)
    #
    # def test_get_category_details(self):
    #     expected_category_detail = {'id': 1, 'category_name': 'test_top_category', 'top_category': None,
    #                                 'sub_category': [
    #                                     {'id': 2, 'category_name': 'test_sub_category', 'top_category': {'id': 1},
    #                                      'sub_category': []}]}
    #
    #     response = self.client.get('/catalog/categories/1/')
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), expected_category_detail)

    def test_post_categories(self):
        test_json = json.dumps({
            "category_name": "parent",
            "top_category": None,
            "sub_category": []})

        # TBD get top cat id
        test_json_child = {
            "category_name": "child",
            "top_category": {"id": 3},
            "sub_category": []
        }
        response = self.client.post('/catalog/categories/', data=test_json, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/catalog/categories/', data=test_json_child, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/catalog/categories/4/')
        response_dict = response.json()
        actual_top_cat = response.json()['top_category']
        print('----------------------', actual_top_cat)
        self.assertTrue(actual_top_cat)

