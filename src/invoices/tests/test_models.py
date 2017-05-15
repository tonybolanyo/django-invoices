import datetime

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from ..models import Invoice


class InvoiceModelTestCase(TestCase):
    """Tests for Invoice class"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.first_name = 'Test name'
        self.last_name = 'Test Last Name'
        self.street = 'Street name, 33'
        self.city = 'City name'
        self.country = 'ES'
        self.state = 'State name'
        self.zipcode = 'ES46000'
        self.invoice = Invoice(
            first_name=self.first_name, last_name=self.last_name,
            street=self.street, city=self.city, state=self.state,
            zipcode=self.zipcode)

    def test_model_can_create_an_invoice(self):
        """Invoice model can create an invoice"""
        old_count = Invoice.objects.count()
        self.invoice.save()
        new_count = Invoice.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_number_one_for_first_invoice_in_year(self):
        """First invoice in the year must be one"""
        invoice = Invoice(
            first_name=self.first_name, last_name=self.last_name,
            street=self.street, city=self.city, state=self.state,
            zipcode=self.zipcode, date=datetime.date(2000, 5, 6))
        invoice.save()
        self.assertEqual(invoice.number, 1)

    def test_new_invoice_next_number(self):
        """New invoice must have next number in the year (no gap)"""
        last_invoice = Invoice(
            first_name=self.first_name, last_name=self.last_name,
            street=self.street, city=self.city, state=self.state,
            zipcode=self.zipcode, date=datetime.date(2000, 5, 6))
        last_invoice.save()
        new_invoice = Invoice(
            first_name=self.first_name, last_name=self.last_name,
            street=self.street, city=self.city, state=self.state,
            zipcode=self.zipcode, date=datetime.date(2000, 5, 6))
        new_invoice.save()
        self.assertEqual(new_invoice.number, last_invoice.number+1)
