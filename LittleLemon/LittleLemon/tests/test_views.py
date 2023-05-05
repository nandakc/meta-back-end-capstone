from django.test import TestCase
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from Restaurant import models
from Restaurant import serializers

class MenuViewTest(TestCase):
    data = []
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        item = models.Menu.objects.create(Title="Item1", Price=11.0, Inventory=10)
        serializer = serializers.MenuSerializer(item)
        self.data.append(serializer.data)
        item = models.Menu.objects.create(Title="Item2", Price=2.22, Inventory=20)
        serializer = serializers.MenuSerializer(item)
        self.data.append(serializer.data)
        print("self.data: " + str(self.data))
        print("setUp: done")

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)

        print("response: " + str(response.content))
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        print("data: " + str(data))
        self.assertEqual(data, self.data)
