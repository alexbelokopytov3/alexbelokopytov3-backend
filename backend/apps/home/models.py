from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

def url_directory(instance, filename):
        return 'posts/{0}/%Y%m%d/{1}'.format(instance.user.id, filename)

class Post(models.Model):

    author_post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True)
    title_post = models.CharField(max_length=200)
    text_post = models.TextField()
    image_posts = models.ImageField(upload_to=url_directory, blank=True)
    create_date_post = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title