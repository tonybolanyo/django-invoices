from django.contrib import admin

from .models import Invoice


class InvoiceAdmin(admin.ModelAdmin):

    list_display = ('full_number', 'date', 'first_name', 'last_name', 'status')
    list_editable = ('status',)

    class Meta:
        model = Invoice

admin.site.register(Invoice, InvoiceAdmin)
