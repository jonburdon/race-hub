from django.test import TestCase
from .forms import TimeOnlyResultForm
from .models import Result

# Create your tests here.
"""
class TimeOnlyResultForm(TestCase):

    def test_item_chiptime_is_required(self):
        form = TimeOnlyResultForm({'chiptime': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('chiptime', form.errors.keys())
        self.assertEqual(form.errors['chiptime'][0], 'This field is required.')

    def test_hyperlink_field_is_not_required(self):
        form = TimeOnlyResultForm({'hyperlink': 'https://www.strava.com'})
        self.assertTrue(form.is_valid())