from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class InvoicesConfig(AppConfig):
    name = 'invoices'
    verbose_name = _('invoices')
