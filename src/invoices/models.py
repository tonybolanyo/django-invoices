import logging
from datetime import date
from decimal import Decimal

from django.db import models

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
        ('new', 'nueva'),
        ('pending', 'pendiente de cobro'),
        ('paid', 'pagada')
    )

    date = models.DateField('fecha', default=date.today)
    number = models.IntegerField('número', default=0)
    first_name = models.CharField('nombre', max_length=200)
    last_name = models.CharField('apellidos', max_length=200)
    street = models.CharField('calle', max_length=120)
    city = models.CharField('ciudad', max_length=120)
    state = models.CharField('estado o provincia', max_length=120)
    zipcode = models.CharField('cód. postal', max_length=120)
    country = CountryField('pais', blank=True, blank_label='selecciona país')
    vat_number = models.CharField('NIF/CIF', max_length=15, blank=True)
    email = email = models.EmailField('email', blank=True)

    def full_number(self):
        return "{year}/{number:06}".format(
            year=self.date.year,
            number=self.number
            )

    class Meta:
        verbose_name = 'factura'
        verbose_name_plural = 'facturas'
        ordering = ('-date', '-number')

    def str(self):
        return 'Factura %s' % self.full_number
