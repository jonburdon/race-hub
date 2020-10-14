from django.test import TestCase
from .models import Result
# Create your tests here.


class TestViews(TestCase):

    def test_all_result_lists(self):
        response = self.client.get('/results/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'results/results.html')

