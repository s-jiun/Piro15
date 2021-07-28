from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']