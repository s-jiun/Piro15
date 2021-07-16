from django.db import models

# Create your models here.

class Item(models.Model):
    product_name = models.CharField(verbose_name='제품명', max_length=100)
    content = models.TextField(verbose_name='내용', blank=True)
    price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
