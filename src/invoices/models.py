import logging
from datetime import date
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField
from model_utils import Choices
from model_utils.models import (
    SoftDeletableModel, StatusModel, TimeStampedModel)

logger = logging.getLogger(__name__)


class Invoice(SoftDeletableModel, StatusModel, TimeStampedModel):

    """
    Invoice main data.
    """

    STATUS = Choices(
        ('new', _('new')),
        ('pending', _('pending')),
        ('paid', _('paid'))
    )

    date = models.DateField(_('date'), default=date.today)
    number = models.IntegerField(_('number'), default=0)
    first_name = models.CharField(_('first name'), max_length=200)
    last_name = models.CharField(_('last name'), max_length=200)
    street = models.CharField(_('street'), max_length=120)
    city = models.CharField(_('city'), max_length=120)
    state = models.CharField(_('state or province'), max_length=120)
    zipcode = models.CharField(_('postal code'), max_length=120)
    country = CountryField(_('country'), blank=True, blank_label='selecciona país')
    vat_number = models.CharField(_('VAT number'), max_length=15, blank=True)
    email = email = models.EmailField(_('email'), blank=True)

    def full_number(self):
        return "{year}/{number:06}".format(
            year=self.date.year,
            number=self.number
            )

    class Meta:
        verbose_name = _('invoice')
        verbose_name_plural = _('invoices')
        ordering = ('-date', '-number')

    def str(self):
        return _('Invoice {number}').format(number=self.full_number)


class InvoiceEntry(TimeStampedModel):

    """
    Entry for one product, service or item included in one invoice.
    """

    description = models.CharField(_('description'), max_length=1024)
    unit = models.CharField(_('unit'), max_length=1024, blank=True, null=True)
    quantity = models.DecimalField(
        _('quantity'), max_digits=19, decimal_places=4,
        validators=[MinValueValidator(0.0)])
    unit_price = models.DecimalField(
        _('unit price'), max_digits=19, decimal_places=4)
    invoice = models.ForeignKey(Invoice, related_name='invoice_entries')
