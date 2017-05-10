from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import Invoice, InvoiceEntry
from .serializers import InvoiceSerializer, InvoiceEntrySerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceEntryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = InvoiceEntry.objects.all()
    serializer_class = InvoiceEntrySerializer
