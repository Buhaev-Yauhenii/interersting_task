import datetime
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """manager for user"""

    def create_user(self, email, password=None, **kwargs):
        """create save and return new user"""
        if not email:
            raise ValueError('user must have email')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        """function for creating superuser"""

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    