from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


class InvoiceViewSetTestCase(TestCase):
    """Test suite for the invoice viewset"""

    def setUp(self):
        """Define the test client and other variables"""

        user = User.objects.create(username='nerd', is_staff=True)

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.invoice_data = {
            "first_name": "Test name",
            "last_name": "Test Last Name",
            "street": "Street name, 33",
            "city": "City name",
            "country": "ES",
            "state": "State name",
            "zipcode": "ES46000",
            "invoice_entries": []
        }
        self.response = self.client.post(
            reverse('invoice-list'),
            self.invoice_data,
            format='json')

    def test_api_can_create_invoice(self):
        """Can create an invoice from json API"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
