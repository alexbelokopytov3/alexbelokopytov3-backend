from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

def url_directory(instance, filename):
        return 'posts/{0}/{1}/{2}'.format(instance.author_post, instance.id, filename)

NEWS_CHOICES = [
    ('sport', 'Sport'),
    ('economics', 'Economics'),
    ('science', 'Science'),
]

class Post(models.Model):

    author_post = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    category_post = models.CharField(max_length=200, blank=True, choices=NEWS_CHOICES)
    title_post = models.CharField(max_length=200)
    text_post = models.TextField()
    image_posts = models.ImageField(upload_to=url_directory, blank=True, null=True)
    create_date_post = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title_post


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    # comment_author = models.CharField(max_length=200)
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    comment_create_date = models.DateTimeField(default=timezone.now)
    comment_text = models.TextField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment_text
