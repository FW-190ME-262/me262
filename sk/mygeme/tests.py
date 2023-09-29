# from django.test import TestCase
# from django.test import SimpleTestCase
from django.test import TestCase

# class SimpleTests(SimpleTestCase):
#     def test_main_page_status_code(self):
#         response = self.client.get('home')
#         self.assertEqual(response.status_code, 304)
from unittest import TestCase

import self as self

from .models import Cat


class Training:
    objects = None


class TrainingModelTestCase(TestCase):


    def setUp(self):
        self.cat = Cat.objects.create(
            name='Test',
            color='Test',
            cyes='Test',
            ears='Test',
            tail='Test')

    def test_training_name(self):
        self.assertEqual(str(self.cat.name), 'Test')

    def test_training_color(self):
        self.assertEqual(str(self.cat.color), 'Test')

    def test_training_cyes(self):
        self.assertEqual(str(self.cat.cyes), 'Test')

    def test_training_ears(self):
        self.assertEqual(str(self.cat.ears), 'Test')

    def test_training_tail(self):
        self.assertEqual(str(self.cat.tail), 'Test')
