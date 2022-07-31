from django.db import models

from django.utils import timezone
from django.conf import settings
# Create your models here.


class WebUsers(models.Model):
    FirstName = models.CharField(max_length=35)
    LastName = models.CharField(max_length=35)
    Password = models.CharField(max_length=20)
    Mail = models.EmailField(max_length=254)
    Register_date = models.DateField(default=timezone.now)
