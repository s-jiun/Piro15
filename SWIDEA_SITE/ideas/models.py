from django.db import models
from devtools.models import DevTool

# Create your models here.

class Idea(models.Model):
    name = models.CharField(max_length=100, help_text="아이다어명을 입력하세요")
    image = models.ImageField(blank=True, null=True, upload_to = 'idea_image/%Y/%m/%d/')
    desc = models.TextField(help_text="아이디어에 대한 설명을 적어주세요")
    likes = models.PositiveIntegerField(default=0)