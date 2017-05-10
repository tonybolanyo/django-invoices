from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Invoice


User = get_user_model()


class InvoiceModelTestCase(TestCase):
    """Tests for Invoice class"""

    def setUp(self):
        """Define the test client and other test variables"""
        first_name = 'Test name'
        last_name = 'Test Last Name'
        street = 'Street name, 33'
        city = 'City name'
        country = 'ES'
        state = 'State name'
        zipcode = 'ES46000'
        self.invoice = Invoice(
            first_name=first_name, last_name=last_name, street=street,
            city=city, state=state, zipcode=zipcode)

    def test_model_can_create_an_invoice(self):
        """Invoice model can create an invoice"""
        old_count = Invoice.objects.count()
        self.invoice.save()
        new_count = Invoice.objects.count()
        self.assertNotEqual(old_count, new_count)


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
