
from PIL import Image as pilImage

from reportlab.lib.colors import black, red
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
logo_filename = './logo.jpg'
styles = getSampleStyleSheet()


def get_logo_size(logo_filename):
    logo_image = pilImage.open(logo_filename)
    width, height = logo_image.size
    logo_w = width/height * LOGO_HEIGHT
    logo_h = LOGO_HEIGHT
    logo_image.close()
    return logo_w, logo_h


def first_page_info(canvas, doc):
    provider_rect(canvas, doc)
    customer_rect(canvas, doc)


title = 'Hello world'
pageinfo = 'platypus example'


class InvoiceTemplate(BaseDocTemplate):

    first_page_tpl = None

    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        BaseDocTemplate.__init__(self, filename, **kw)
        first_page_tpl = PageTemplate(
            'normal', 
            [Frame(2*cm, 2*cm, 17*cm, 25.7*cm, id='F1')],
            onPage=self._customer_and_provider)
        self.addPageTemplates(first_page_tpl)


    def _customer_and_provider(self, canvas, doc):
        self._provider_rect(canvas, doc)
        self._general_data_rect(canvas, doc)
        self._customer_rect(canvas, doc)
        self._items_rect(canvas, doc)
        self._payment_rect(canvas, doc)
        self._totals_rect(canvas, doc)

    def _provider_rect(self, canvas, doc):
        canvas.saveState()
        top = 19.7*cm
        left = 2*cm
        width = 7*cm
        height = 3.5*cm
        canvas.setStrokeColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.restoreState()

    def _general_data_rect(self, canvas, doc):
        canvas.saveState()
        top = 19.7*cm
        left = 12*cm
        width = 7*cm
        height = 3.5*cm
        canvas.setStrokeColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.drawCentredString(15.5*cm, 22.5*cm, 'FACTURA')
        canvas.restoreState()

    def _customer_rect(self, canvas, doc):
        canvas.saveState()
        top = 15.4*cm
        left = 2*cm
        width = 17*cm
        height = 3.5*cm
        canvas.setStrokeColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.restoreState()

    def _items_rect(self, canvas, doc):
        canvas.saveState()
        top = 6.6*cm
        left = 2*cm
        width = 17*cm
        height = 8.5*cm
        canvas.setStrokeColor(red)
        canvas.setFillColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.rect(left, top+8*cm, width, .5*cm, stroke=1, fill=1)
        #canvas.
        canvas.restoreState()

    def _payment_rect(self, canvas, doc):
        canvas.saveState()
        top = 3.8*cm
        left = 2*cm
        width = 7*cm
        height = 2.5*cm
        canvas.setStrokeColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.restoreState()

    def _totals_rect(self, canvas, doc):
        canvas.saveState()
        top = 3.8*cm
        left = 12*cm
        width = 7*cm
        height = 2.5*cm
        canvas.setStrokeColor(red)
        canvas.setLineWidth(.5)
        canvas.rect(left, top, width, height, stroke=1)
        canvas.restoreState()





doc = InvoiceTemplate(
    "invoice.pdf", pagesize=A4, author='Ana Belchí', 
    title='Factura', subject='Prueba', creator='anabelchi.com', 
    producer='anabelchi.com', compress='1', showBoundary=0)
print(doc.height, doc.width)
Story = []
style = styles["Normal"]
logo_w, logo_h = get_logo_size(logo_filename)
logo = Image(logo_filename, height=logo_h, width=logo_w)
logo.hAlign = 'CENTER'
Story.append(logo)
Story.append(Spacer(1, 2*cm))
doc.build(Story)#, onFirstPage=first_page_info)
