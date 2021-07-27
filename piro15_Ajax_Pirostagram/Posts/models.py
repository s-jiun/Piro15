from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(blank=True, null=True)
    writer = models.CharField(max_length=50)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)