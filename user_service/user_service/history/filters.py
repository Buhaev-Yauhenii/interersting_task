import django_filters
from history.models import TransactionsHistory

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = TransactionsHistory
        fields = {
            'sum': ['lt', 'gt', 'exact'],
            'time_of_transaction': ['exact', 'year__gt', 'year__lt'],
        }
