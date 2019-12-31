from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Invoice

User = get_user_model()


class InvoiceListViewTestCase(TestCase):
    """Test suite for the invoice list view"""

    def setUp(self):
        """Define the test client and other variables"""

        user = User.objects.create(username="nerd", is_staff=True)

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
        }

    def test_api_can_create_invoice(self):
        """Can create an invoice from json API"""
        self.response = self.client.post(
            reverse("invoice-list"), self.invoice_data, format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class InvoiceDetailViewTestCase(TestCase):
    """Test suite for invoice detail view"""

    def setUp(self):
        """Define the test client and other variables"""

        user = User.objects.create(username="nerd", is_staff=True)

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
        }

    def test_can_retrieve_invoice_data(self):
        """Can retrieve an existing invoice"""
        invoice = mixer.blend(Invoice)
        self.response = self.client.get(
            reverse("invoice-detail", kwargs={"pk": invoice.pk}), format="json"
        )
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_can_delete_invoice(self):
        """Can delete an invoice"""
        invoice = mixer.blend(Invoice)
        old_count = Invoice.objects.count()
        self.response = self.client.delete(
            reverse("invoice-detail", kwargs={"pk": invoice.pk}), format="json"
        )
        new_count = Invoice.objects.count()
        self.assertEqual(new_count, old_count - 1)
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_update_invoice(self):
        """Can update invoice"""
        invoice = mixer.blend(Invoice)
        self.response = self.client.put(
            reverse("invoice-detail", kwargs={"pk": invoice.pk}),
            self.invoice_data,
            format="json",
        )
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
