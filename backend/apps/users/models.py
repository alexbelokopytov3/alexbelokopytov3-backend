from django.db import models
from django.conf import settings
# Create your models here.

def url_directory(instance, filename):
        return 'user/{0}/profile_photo/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=18, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=url_directory, blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)