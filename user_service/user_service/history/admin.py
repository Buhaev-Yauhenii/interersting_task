from django.contrib import admin
from .models import TransactionsHistory
# Register your models here.

class HistoryAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['user_id', 'sum',
                    'time_of_transaction',
                    'category',
                    'organization',
                    'description']
    readonly_fields = ['user_id',
                       'sum',
                       'time_of_transaction',
                       'category',
                       'organization',
                       'description']
    search_fields = ['sum', 'time_of_transaction']


admin.site.register(TransactionsHistory, HistoryAdmin)