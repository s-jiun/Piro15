from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'short_cont']
    list_display_links = ['title']
    list_filter = ['created_at']
    search_fields = ['title']

    def short_cont(self, post):
        return post.content[:20]

# Register your models here.
