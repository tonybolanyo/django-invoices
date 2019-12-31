from django.test import TestCase

from ..utils import InvoiceTemplate


class InvoiceTemplateTestCase(TestCase):

    """Test suite for class InvoiceTemplate"""

    # def test_has_get_logo_size(self):
    #     """
    #     Has a get_logo_size function that returns width and height for
    #     print logo in pdf document.
    #     """
    #     tpl = InvoiceTemplate('test_invoice.pdf')
    #     assert tpl is not None
    #     w, h = tpl.get_logo_size()
    #     assert w > 0
    #     assert h > 0
