from django.urls import path

app_name = 'user'
from history import views
from history.models import TransactionsHistory

urlpatterns = [
    path('/transactions', views.CreateHistoryAPIView.as_view(), name="history"),
]
