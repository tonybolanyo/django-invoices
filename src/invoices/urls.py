from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import views

schema_view = get_schema_view(title='django-invoices API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'entries', views.InvoiceEntryViewSet)

urlpatterns = [
    # url(r'^$', views.api_root),
    # url(r'^invoices/$',
    #     views.InvoiceListView.as_view(), name='invoice-list'),
    # url(r'^invoices/(?P<pk>\d+)/$',
    #     views.InvoiceDetailView.as_view(), name='invoice-detail'),
    # url(r'^entries/$',
    #     views.InvoiceEntryListView.as_view(), name='invoiceentry-list'),
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
]
