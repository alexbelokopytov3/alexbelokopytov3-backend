from django.db import models

from django.utils import timezone
from django.conf import settings
# Create your models here.


class Registration(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mail = models.EmailField(max_length=254)
    phone = models.IntegerField()
    register_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.id