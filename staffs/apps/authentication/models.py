from datetime import datetime as date_time
from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.db import models

import jwt


class Role(models.Model):
    """
    create a employee roles/positions
    """
    name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    # database to improve lookup performance.
    username = models.CharField(db_index=True, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.ForeignKey(Role, related_name='users',
                             on_delete=models.CASCADE, blank=True, null=True)
    line_manager = models.ForeignKey(
        'self', related_name='employee_manager',
        on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case, we want that to be the email field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self.generate_jwt_token()

    def generate_jwt_token(self):
        """This method generates a JSON Web Token """
        user_details = {'email': self.email,
                        'username': self.username,
                        'first_name': self.first_name,
                        'last_name': self.last_name
                        }
        token = jwt.encode(
            {
                'user_data': user_details,
                'exp': date_time.now() + timedelta(days=7)
            }, settings.SECRET_KEY, algorithm='HS256'
        )
        return token.decode('utf-8')
