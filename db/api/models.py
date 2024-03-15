from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(null=True)
    last_name = models.CharField(null=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True)


class Role(models.Model):
    role_name = models.CharField(max_length=50, null=False)


class Resource(models.Model):
    name = models. CharField(max_length=25, default=None, null=True)
    in_stock = models. CharField(max_length=15, default=None, null=True)
    spent_per_month = models. CharField(max_length=15, default=None, null=True)
    spent_in_total = models.CharField(max_length=15, default=None, null=True)