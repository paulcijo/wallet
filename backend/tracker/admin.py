from django.contrib import admin
from .models import Transaction
from django.contrib.admin import DateFieldListFilter
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display=('item', 'cost', 'date', 'transaction_type', 'necessary', 'notes')
    list_filter = (('date', DateFieldListFilter),'transaction_type', 'necessary')
    list_editable = ('cost',)
    search_fields = ('item','notes',)

admin.site.register(Transaction, TransactionAdmin)