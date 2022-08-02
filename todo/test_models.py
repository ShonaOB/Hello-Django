from django.test import TestCase
from .models import Item

# Create your tests here.


class TestDjango(TestCase):

    def test_this_thing_works(self):
        self.assertEqual(1, 1)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')