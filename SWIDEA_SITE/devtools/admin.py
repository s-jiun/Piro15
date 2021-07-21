from django.contrib import admin
from .models import DevTool

# Register your models here.

@admin.register(DevTool)
class DevToolAdmin(admin.ModelAdmin):
    list_display = ['pk', 'tool_name', 'type']