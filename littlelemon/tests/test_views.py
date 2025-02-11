from django.test import TestCase
from .models import Menu
from rest_framework.test import APIClient
from serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        # Add test data
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="Pizza", price=200, inventory=50)
        self.item2 = Menu.objects.create(title="Burger", price=150, inventory=30)

    def test_getall(self):
        # Make a GET request to the Menu endpoint
        response = self.client.get('/menu-items/')

        # Serialize the expected data
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        # Assert the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)