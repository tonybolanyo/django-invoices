import datetime

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Invoice, InvoiceEntry


class InvoiceModelTestCase(TestCase):
    """Tests for Invoice class"""

    def test_model_can_create_an_invoice(self):
        """Invoice model can create an invoice"""
        old_count = Invoice.objects.count()
        invoice = mixer.blend(Invoice)
        new_count = Invoice.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_number_one_for_first_invoice_in_year(self):
        """First invoice in the year must be one"""
        invoice = mixer.blend(Invoice)
        self.assertEqual(invoice.number, 1)

    def test_new_invoice_next_number(self):
        """New invoice must have next number in the year (no gap)"""
        last_invoice = mixer.blend(Invoice, date=datetime.date(2000, 10, 1))
        new_invoice = mixer.blend(Invoice, date=datetime.date(2000, 10, 1))
        self.assertEqual(new_invoice.number, last_invoice.number+1)

    def test_full_number_include_year_and_number(self):
        """Has property full_number including year and number"""
        invoice = mixer.blend(Invoice)
        assert str(invoice.date.year) in invoice.full_number
        assert str(invoice.number) in invoice.full_number

    def test_str_contains_year_and_number(self):
        """str contains year and number"""
        invoice = mixer.blend(Invoice)
        assert str(invoice.date.year) in str(invoice)
        assert str(invoice.number) in str(invoice)


class InvoiceEntryModelTest(TestCase):

    def test_can_create_invoice_entry(self):
        """Can create invoice entry line"""
        old_count = InvoiceEntry.objects.count()
        entry = mixer.blend(InvoiceEntry)
        new_count = InvoiceEntry.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_first_entry_has_first_position(self):
        """First entry should have first position"""
        entry = mixer.blend(InvoiceEntry)
        self.assertEqual(entry.position, 1)

    def test_has_total_calculation(self):
        """Invoice entry has total calculation"""
        entry = mixer.blend(InvoiceEntry, quantity=1.5, unit_price=2.5)
        self.assertEqual(entry.total, 3.75)

    def test_position_automated_calculation(self):
        """New entry has next position"""
        invoice = mixer.blend(Invoice)
        entry_one = mixer.blend(InvoiceEntry, invoice=invoice)
        entry_two = mixer.blend(InvoiceEntry, invoice=invoice)
        self.assertEqual(entry_one.position, 1)
        self.assertEqual(entry_two.position, 2)

    def test_entry_str_contains_description(self):
        """InvoiceEntry str contains description"""
        entry = mixer.blend(InvoiceEntry)
        assert entry.description in str(entry)
