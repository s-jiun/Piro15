from re import T
from django.db import models
from django.conf import settings
from django.db.models.base import Model

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return f'<{self.pk}> {self.name}'
    
    class Meta:
        ordering = ['id']


#class Post(models.Model):
#    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)