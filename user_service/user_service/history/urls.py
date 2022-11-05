from django.urls import path
app_name = 'user'
from history import views

urlpatterns = [
    path('/create_transaction', views.CreateHistoryAPIView.as_view(), name="history")
]