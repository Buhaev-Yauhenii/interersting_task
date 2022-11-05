from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from history.serializers import HistorySerializer
from rest_framework.permissions import IsAuthenticated

class CreateHistoryAPIView(generics.CreateAPIView):
    """class for create view of user"""
    serializer_class = HistorySerializer
