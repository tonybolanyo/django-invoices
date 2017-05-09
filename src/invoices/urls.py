from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^invoices/$', views.InvoiceList.as_view()),
    url(r'^invoices/(?P<pk>\d+)/$', views.InvoiceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)