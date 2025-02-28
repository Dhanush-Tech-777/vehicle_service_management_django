from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Component

class ViewTests(TestCase):

    def setUp(self):
        """Initialize test client and test data"""
        self.client = APIClient()
        self.component = Component.objects.create(name="Brake Pad", price=50.00)
        self.component_url = reverse("component-list")  # Adjust based on your router names

    def test_get_components(self):
        """Test retrieving components list"""
        response = self.client.get(self.component_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Brake Pad")

    def test_create_component(self):
        """Test creating a new component"""
        response = self.client.post(self.component_url, {"name": "Oil Filter", "price": 20.00})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Component.objects.count(), 2)
