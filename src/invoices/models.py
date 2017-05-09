import logging
from datetime import date
from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField
from model_utils import Choices
from model_utils.models import (
    SoftDeletableModel, StatusModel, TimeStampedModel)

logger = logging.getLogger(__name__)


class Invoice(SoftDeletableModel, StatusModel, TimeStampedModel):

    """
    Representación de la cabecera de una factura.
    """

    STATUS = Choices(
        ('new', _('new')),
        ('pending', _('pending')),
        ('paid', _('paid'))
    )

    date = models.DateField('date', default=date.today)
    number = models.IntegerField('number', default=0)
    first_name = models.CharField('first name', max_length=200)
    last_name = models.CharField('last name', max_length=200)
    street = models.CharField('street', max_length=120)
    city = models.CharField('city', max_length=120)
    state = models.CharField('state or province', max_length=120)
    zipcode = models.CharField('postal code', max_length=120)
    country = CountryField('country', blank=True, blank_label='selecciona país')
    vat_number = models.CharField('VAT number', max_length=15, blank=True)
    email = email = models.EmailField('email', blank=True)

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
