from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from history.serializers import HistorySerializer
from rest_framework.permissions import IsAuthenticated
from history.models import TransactionsHistory
from app.email import preset_email

from django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    min_sum = filters.NumberFilter(field_name="sum", lookup_expr='gte')
    max_sum = filters.NumberFilter(field_name="sum", lookup_expr='lte')
    min_year = filters.NumberFilter(field_name="time_of_transaction", lookup_expr='year__gt')
    max_year = filters.NumberFilter(field_name="time_of_transaction", lookup_expr='year__lt')

    class Meta:
        model = TransactionsHistory
        fields = ['category', 'sum']


class CreateHistoryAPIView(generics.ListCreateAPIView):
    """class for create view of user"""
    serializer_class = HistorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_queryset(self):
        preset_email()
        return TransactionsHistory.objects.filter(email=self.request.user)
