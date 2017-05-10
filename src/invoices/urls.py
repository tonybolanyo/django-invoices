from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'entries', views.InvoiceEntryViewSet)

urlpatterns = [
    # url(r'^$', views.api_root),
    url(r'^', include(router.urls)),
]
