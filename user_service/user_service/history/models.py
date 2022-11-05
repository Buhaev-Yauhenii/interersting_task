from django.db import models
from user.models import User
from django.utils import timezone
from djmoney.models.fields import MoneyField
 

# Create your models here.
class TransactionsHistory(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    sum = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    time_of_transaction = models.DateTimeField(default=timezone.now)
    category = models.JSONField(default=list, blank=True,)
    organization = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

