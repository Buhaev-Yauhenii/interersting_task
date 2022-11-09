from django.utils import timezone
from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin, )

from user import manager


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""

    email = models.EmailField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    categories = models.TextField(null=True, blank=True)
    objects = manager.UserManager()

    USERNAME_FIELD = 'email'
