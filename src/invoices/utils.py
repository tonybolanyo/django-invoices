
from PIL import Image as pilImage

from reportlab.lib.colors import black, red
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
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

LOGO_HEIGHT = 3*cm
logo_filename = 'invoices/logo.jpg'
styles = getSampleStyleSheet()


def get_logo_size(logo_filename):
    logo_image = pilImage.open(logo_filename)
    width, height = logo_image.size
    logo_w = width/height * LOGO_HEIGHT
    logo_h = LOGO_HEIGHT
    logo_image.close()
    return logo_w, logo_h


def provider_rect(canvas, doc):
    canvas.saveState()
    top = 18*cm
    left = 2*cm
    width = 7*cm
    height = 5*cm
    canvas.setStrokeColor(red)
    canvas.setLineWidth(.3)
    canvas.rect(left, top, width, height, stroke=1)
    canvas.restoreState()


def customer_rect(canvas, doc):
    canvas.saveState()
    top = 18*cm
    left = 12*cm
    width = 7*cm
    height = 5*cm
    canvas.setStrokeColor(red)
    canvas.setLineWidth(.3)
    canvas.rect(left, top, width, height, stroke=1)
    canvas.restoreState()


def first_page_info(canvas, doc):
    provider_rect(canvas, doc)
    customer_rect(canvas, doc)


title = 'Hello world'
pageinfo = 'platypus example'


doc = SimpleDocTemplate("invoice.pdf")
Story = []
style = styles["Normal"]
logo_w, logo_h = get_logo_size(logo_filename)
logo = Image(logo_filename, height=logo_h, width=logo_w)
logo.hAlign = 'CENTER'
Story.append(logo)
Story.append(Spacer(1, 2*cm))
doc.build(Story, onFirstPage=first_page_info)
