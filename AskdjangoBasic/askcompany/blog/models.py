from django.db import models
from django.conf import settings
from askcompany.utils import uuid_upload_to

# Create your models here.

class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField()
    photo = models.ImageField(blank = True, upload_to = uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()