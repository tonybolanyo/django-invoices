from rest_framework import serializers

from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = ('id', 'date', 'number', 'first_name', 'last_name', 'street',
                  'city', 'state', 'zipcode', 'country', 'vat_number', 'email')
        
