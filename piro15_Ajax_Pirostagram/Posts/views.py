from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts':posts}

    return render(request, template_name='post_list.html', context=ctx)