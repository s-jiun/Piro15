from re import T
from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.urls import reverse
from askcompany.utils import uuid_upload_to

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank = True, upload_to = uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return f'<{self.pk}> {self.name}'
    
    class Meta:
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.pk])
        #return reverse('shop:item_detail', kwargs={'pk':self.pk})


#class Post(models.Model):
#    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)