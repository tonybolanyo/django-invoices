from rest_framework import generics, mixins

from .models import Invoice
from .serializers import InvoiceSerializer


class InvoiceList(generics.ListCreateAPIView):
    """
    List all the invoices (GET) or create a new one (POST)
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a invoice instance.
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
