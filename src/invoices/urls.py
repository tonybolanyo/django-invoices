from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
	url(r'^$', views.api_root),
    url(r'^invoices/$', views.InvoiceList.as_view(), name='invoice-list'),
    url(r'^invoices/(?P<pk>\d+)/$', views.InvoiceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)