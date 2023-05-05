from django.test import TestCase
from Restaurant import models

class MenuTest(TestCase):
    def test_get_item(self):
        item = models.Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")