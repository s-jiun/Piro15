from django.db import models
from devtools.models import DevTool

# Create your models here.

class Idea(models.Model):
    title = models.CharField(max_length=100, help_text="아이다어명을 입력하세요")
    image = models.ImageField(null=True, upload_to = 'idea_image/%Y/%m/%d/')
    content = models.TextField(blank=True, help_text="아이디어에 대한 설명을 적어주세요")
    interest = models.PositiveIntegerField(default=0)

    DEVTOOL_CHOICES = DevTool.objects.values_list('name', 'name').order_by('id')

    devtool = models.CharField(max_length=50, choices=DEVTOOL_CHOICES, null=True)