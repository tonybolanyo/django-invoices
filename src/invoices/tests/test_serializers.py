from django.test import TestCase

from mixer.backend.django import mixer

from ..models import Invoice, InvoiceEntry
from ..serializers import InvoiceSerializer, InvoiceEntrySerializer


class InvoiceSerializerTestCase(TestCase):

    def test_invoice_fields(self):
        """Invoice serializer has all relevant fields"""
        invoice = mixer.blend(Invoice)
        serializer = InvoiceSerializer(instance=invoice)
        data = serializer.data

        self.assertEqual(set(data.keys()), set([
            'id', 'date', 'number', 'first_name', 'last_name', 'street',
            'city', 'state', 'zipcode', 'country', 'vat_number', 'email',
            'payment_method', 'notes', 'invoice_entries']))


class InvoiceEntrySerializerTestCase(TestCase):

    def test_entry_fields(self):
        """Invoice entry has all relevant fields"""
        entry = mixer.blend(InvoiceEntry)
        serializer = InvoiceEntrySerializer(instance=entry)
        data = serializer.data
        self.assertEqual(set(data.keys()), set([
            'invoice', 'description', 'unit', 'quantity', 'unit_price']))
