from django.http import request, HttpResponse, HttpRequest
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from history.models import TransactionsHistory 
from user.models import User
from rest_framework.permissions import IsAuthenticated
from django.db import transaction,IntegrityError
from django.db.models import F

import json


class HistorySerializer(serializers.ModelSerializer):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_user_email(cls):
        request = cls.context.get("request")
        return str(request.user)

    class Meta:
        model = TransactionsHistory
        fields = ['category', 'sum', 'organization', 'description', ]
        

    def create(self, validated_data):
        user_email = self.get_user_email()
        
        try:
            with transaction.atomic():
                
                unit = TransactionsHistory(
                                    user_id = User.objects.get(email = user_email),
                                    sum=validated_data['sum'],
                                        category=validated_data['category'],
                                        organization=validated_data['organization'],
                                        description=validated_data['description'])
                unit.save()

                User.objects.filter(email = user_email).update(balance=F("balance") - validated_data['sum'])
                
                categories = User.objects.get(email = 'admin@admin.com').categories
                test = User.objects.filter(email = 'admin@admin.com').update(categories = F("categories") + ' three')
                print(categories)
                print(test)
                return unit
        except IntegrityError:
            return False
