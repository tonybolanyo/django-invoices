from rest_framework import serializers

from .models import Invoice, InvoiceEntry


class InvoiceEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceEntry
        fields = ('invoice', 'description', 'unit', 'quantity', 'unit_price',)


class InvoiceEntrySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceEntry
        fields = ('position', 'description', 'unit', 'quantity', 'unit_price', 'total',)


class InvoiceSerializer(serializers.ModelSerializer):

    """
    Serialize only invoice head data, not including entries.
    """

    invoice_entries = InvoiceEntrySimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ('id', 'date', 'number', 'first_name', 'last_name', 'street',
                  'city', 'state', 'zipcode', 'country', 'vat_number', 'email',
                  'payment_method', 'notes', 'invoice_entries',)
        read_only_fields = ('id', 'number',)
