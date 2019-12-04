import json

from django.test import TestCase
from django.test import tag
from apps.catalog.models import Category


class SimpleTest(TestCase):

    def setUp(self):
        top_category = Category.objects.create(category_name='test_top_category')
        Category.objects.create(category_name='test_sub_category', top_category=top_category)

    @tag('smoke')
    def test_get_list_smoke(self):
        response = self.client.get('/catalog/categories/')

        self.assertContains(response, "test_top_category", status_code=200)

    def test_get_category_details(self):
        expected_category_detail = {'id': 1, 'category_name': 'test_top_category', 'top_category': None,
                                    'sub_category': [
                                        {'id': 2, 'category_name': 'test_sub_category', 'top_category': {'id': 1},
                                         'sub_category': []}]}

        response = self.client.get('/catalog/categories/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_category_detail)

    def test_post_categories(self):
        latest_id = Category.objects.latest('id').id
        expected_top_id = int(latest_id) + 1
        expected_sub_id = int(latest_id) + 2

        expected_parent_child = {'id': expected_top_id, 'category_name': 'top category', 'top_category': None,
                                 'sub_category': [
                                     {'id': expected_sub_id, 'category_name': 'sub category', 'top_category': {'id': expected_top_id},
                                      'sub_category': []}]}

        tst_top_cat_json = json.dumps({
            "category_name": "top category",
            "top_category": None,
            "sub_category": []})

        tst_sub_cat_json = {
            "category_name": "sub category",
            "top_category": {"id": expected_top_id},
            "sub_category": []
        }
        response = self.client.post('/catalog/categories/', data=tst_top_cat_json, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.post('/catalog/categories/', data=tst_sub_cat_json, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.get('/catalog/categories/3/')
        actual_dict = response.json()

        self.assertEqual(actual_dict, expected_parent_child)
