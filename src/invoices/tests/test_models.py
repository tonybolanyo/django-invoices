import datetime

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from ..models import Invoice, InvoiceEntry


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


class InvoiceEntryModelTest(TestCase):

    def setUp(self):
        first_name = 'Test name'
        last_name = 'Test Last Name'
        street = 'Street name, 33'
        city = 'City name'
        country = 'ES'
        state = 'State name'
        zipcode = 'ES46000'
        self.invoice = Invoice(
            first_name=first_name, last_name=last_name,
            street=street, city=city, state=state,
            zipcode=zipcode)
        self.invoice.save()

    def test_can_create_invoice_entry(self):
        """Can create invoice entry line"""
        old_count = InvoiceEntry.objects.count()
        entry = InvoiceEntry(invoice=self.invoice, description='Test entry')
        entry.save()
        new_count = InvoiceEntry.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_first_entry_has_first_position(self):
        """First entry should have first position"""
        entry = InvoiceEntry(invoice=self.invoice, description='Test entry')
        entry.save()
        self.assertEqual(entry.position, 1)

    def test_has_total_calculation(self):
        """Invoice entry has total calculation"""
        entry = InvoiceEntry(invoice=self.invoice, description='Test entry',
                             quantity=1.5, unit_price=2.5)
        entry.save()
        self.assertEqual(entry.total, 3.75)
