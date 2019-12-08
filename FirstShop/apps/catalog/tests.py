import json

from django.test import TestCase
from django.test import tag
from apps.catalog.models import Category


class SimpleTest(TestCase):
    test_list_url = '/catalog/categories/'
    tst_top_cat_name = 'test_top_category'
    tst_sub_cat_name = 'test_sub_category'

    def setUp(self):
        top_category = Category.objects.create(category_name=self.tst_top_cat_name)
        Category.objects.create(category_name=self.tst_sub_cat_name, top_category=top_category)

    @tag('smoke')
    def test_get_list_smoke(self):
        response = self.client.get(self.test_list_url)
        self.assertContains(response, self.tst_top_cat_name, status_code=200)

    def test_get_category_details(self):
        expected_category_detail = {'id': 1, 'category_name': self.tst_top_cat_name, 'top_category': None,
                                    'sub_category': [
                                        {'id': 2, 'category_name': self.tst_sub_cat_name, 'top_category': {'id': 1},
                                         'sub_category': []}]}

        response = self.client.get(f'{self.test_list_url}1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_category_detail)

    def test_post_categories(self):
        latest_id = Category.objects.latest('id').id
        expected_top_id = int(latest_id) + 1
        expected_sub_id = int(latest_id) + 2
        expected_top_with_sub = {'id': expected_top_id, 'category_name': 'top category', 'top_category': None,
                                 'sub_category': [
                                     {'id': expected_sub_id, 'category_name': 'sub category',
                                      'top_category': {'id': expected_top_id},
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
        response = self.client.post(self.test_list_url, data=tst_top_cat_json, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response = self.client.post(self.test_list_url, data=tst_sub_cat_json, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get(f'{self.test_list_url}{expected_top_id}/')

        self.assertEqual(response.json(), expected_top_with_sub)

    def test_filter_by_category_name(self):
        filter_category_name = self.tst_sub_cat_name

        response = self.client.get(self.test_list_url)
        self.assertTrue(len(response.json()) > 1)

        response = self.client.get(
            self.test_list_url + f'?category_name={filter_category_name}')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) == 1)

        actual_category_name = response.json()[0]['category_name']
        self.assertEqual(actual_category_name, filter_category_name)
