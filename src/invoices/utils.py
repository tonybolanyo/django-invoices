import os
from PIL import Image as pilImage

from django.conf import settings
from django.utils.translation import ugettext as _

from reportlab.lib.colors import black, red, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.platypus.doctemplate import BaseDocTemplate, PageTemplate
from reportlab.platypus.frames import Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm


"""
__init__ params:

    filename, pagesize=defaultPageSize, pageTemplates=[], showBoundary=0,
    leftMargin=inch, rightMargin=inch, topMargin=inch, bottomMargin=inch,
    allowSplitting=1, title=None, author=None, _pageBreakQuick=1,
    encrypt=None

The required filename can be a string, the name of a file to receive the
created PDF document; alternatively it can be an object which has a write
method such as a `BytesIO` or `file` or `socket`.
"""

LOGO_HEIGHT = 4*cm
styles = getSampleStyleSheet()


def first_page_info(canvas, doc):
    provider_rect(canvas, doc)
    customer_rect(canvas, doc)


title = 'Hello world'
pageinfo = 'platypus example'


class InvoiceTemplate(BaseDocTemplate):

    first_page_tpl = None
    margins = {
        'top': 2*cm, 'bottom': 2*cm,
        'left': 2*cm, 'right': 2*cm,
    }
    block_width = 7*cm
    block_height = 3.5*cm
    column_width = 1.5*cm

    label_font = 'Helvetica'
    label_font_size = 10

    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, filename, **kw)
        self.page_width, self.page_height = self.pagesize
        first_page_tpl = PageTemplate(
            'normal',
            [Frame(0, 0, 21*cm, 29.7*cm, id='F1')],
            onPage=self._draw_static_elements)
        self.addPageTemplates(first_page_tpl)

    def _draw_static_elements(self, canvas, doc):
        self._provider_rect(canvas, doc)
        self._general_data_rect(canvas, doc)
        self._customer_rect(canvas, doc)
        self._items_rect(canvas, doc)
        self._payment_rect(canvas, doc)
        self._totals_rect(canvas, doc)
        self._draw_logo(canvas, doc)

    def _provider_rect(self, canvas, doc):
        canvas.saveState()
        top = 19.7*cm
        left = self.margins['left']
        width = self.block_width
        height = self.block_height
        canvas.setStrokeColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.restoreState()

    def _general_data_rect(self, canvas, doc):
        canvas.saveState()
        top = 19.7*cm
        left = self.page_width - self.margins['right'] - self.block_width
        width = self.block_width
        height = self.block_height
        canvas.setStrokeColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.setFillColorRGB(.7, .7, .7)
        canvas.setFont(self.label_font, 25)
        canvas.drawCentredString(15.5*cm, 22.4*cm, _('INVOICE'))
        canvas.restoreState()

    def _customer_rect(self, canvas, doc):
        canvas.saveState()
        top = 15.4*cm
        left = self.margins['left']
        width = self.page_width - self.margins['left'] - self.margins['right']
        height = self.block_height
        canvas.setStrokeColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.restoreState()

    def _items_rect(self, canvas, doc):
        canvas.saveState()
        top = 6.6*cm
        left = self.margins['left']
        width = self.page_width - self.margins['left'] - self.margins['right']
        height = 8.5*cm
        canvas.setStrokeColor(red)
        canvas.setFillColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.rect(left, top+8*cm, width, .5*cm, stroke=1, fill=1)
        left = left + self.column_width
        canvas.line(left, top, left, top + height)
        left = self.page_width - self.margins['right'] - self.column_width
        canvas.line(left, top, left, top + height)
        left = left - self.column_width
        canvas.line(left, top, left, top + height)
        left = left - self.column_width
        canvas.line(left, top, left, top + height)
        left = left - self.column_width
        canvas.line(left, top, left, top + height)

        canvas.setFillColor(white)
        canvas.setFont(self.label_font, self.label_font_size)
        text_top = top + height - .4*cm
        left = self.margins['left'] + self.column_width / 2.0
        canvas.drawCentredString(left, text_top, _('REF.'))
        left = left + (width - self.column_width*5) / 2.0
        canvas.drawCentredString(left, text_top, _('ITEMS'))
        left = left + (width - self.column_width*5) / 2.0 + self.column_width
        canvas.drawCentredString(left, text_top, _('QTY.'))
        left = left + self.column_width
        canvas.drawCentredString(left, text_top, _('€/Unit'))
        left = left + self.column_width
        canvas.drawCentredString(left, text_top, _('DIS.'))
        left = left + self.column_width
        canvas.drawCentredString(left, text_top, _('TOTAL'))
        canvas.restoreState()

    def _payment_rect(self, canvas, doc):
        canvas.saveState()
        top = 3.8*cm
        left = self.margins['left']
        width = self.block_width
        height = self.block_height - 1*cm
        canvas.setStrokeColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.restoreState()

    def _totals_rect(self, canvas, doc):
        canvas.saveState()
        top = 3.8*cm
        left = self.page_width - self.margins['right'] - self.block_width
        width = self.block_width
        height = self.block_height - 1*cm
        canvas.setStrokeColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.setFillColor(red)
        canvas.rect(
            left, top,
            width - self.column_width * 2,
            height, fill=1)
        canvas.restoreState()

    def _draw_logo(self, canvas, doc):
        filename = settings.INVOICES_LOGO_FILENAME
        # filename = os.path.join('..', 'static', 'images', 'logo.jpg')
        logo_image = pilImage.open(filename)
        width, height = logo_image.size
        logo_w = width/height * LOGO_HEIGHT
        logo_h = LOGO_HEIGHT
        logo_x = (self.page_width - logo_w) / 2.0
        logo_y = (self.page_height - logo_h - self.margins['top'])
        logo_image.close()
        canvas.drawImage(filename, logo_x, logo_y, logo_w, logo_h)


doc = InvoiceTemplate(
    "invoice.pdf", pagesize=A4, author='Ana Belchí',
    title='Factura', subject='Prueba', creator='anabelchi.com',
    producer='anabelchi.com', compress='1', showBoundary=0)
Story = []
style = styles["Normal"]
Story.append(Spacer(1, 2*cm))
doc.build(Story)  # , onFirstPage=first_page_info)
