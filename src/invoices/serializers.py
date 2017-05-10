from rest_framework import serializers

from .models import Invoice, InvoiceEntry


class InvoiceEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceEntry
        fields = ('invoice', 'description', 'unit', 'quantity', 'unit_price',)


class InvoiceSerializer(serializers.ModelSerializer):

    invoice_entries = InvoiceEntrySerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('id', 'date', 'number', 'first_name', 'last_name', 'street',
                  'city', 'state', 'zipcode', 'country', 'vat_number', 'email',
                  'invoice_entries',)

    def create(self, validated_data):
        entries_data = validated_data.pop('invoice_entries')
        invoice = Invoice.objects.create(**validated_data)
        assert(invoice is not None)
        for entry_data in entries_data:
            InvoiceEntry.objects.create(invoice=invoice, **entry_data)
        return invoice
