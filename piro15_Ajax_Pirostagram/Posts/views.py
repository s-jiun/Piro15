import json
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Comment, Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts':posts}

    return render(request, template_name='Posts/post_list.html', context=ctx)

def create_post(request, post=None):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('Posts:post_list')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'Posts/create_post.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'Posts/create_post.html', ctx)

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']

    post = Post.objects.get(id=post_id)

    if post.preference == False:
        post.preference = True
    else:
        post.preference = False

    post.save()
    return JsonResponse({'id': post_id})

@csrf_exempt
def add_ajax(request):
    print('view')
    req = json.loads(request.body)
    post_id = req['id']
    content = req['content']
    post=Post.objects.get(id=post_id)
    comment = Comment.objects.create(board=post, text=content)

    post.save()
    return JsonResponse({'post_id': post_id, 'comment_id': comment.id, 'content': comment.text})

@csrf_exempt
def delete_ajax(request):
    req = json.loads(request.body)
    post_id = req['post_id']
    comment_id = req['comment_id']
    post = Post.objects.get(id=post_id)
    Comment.objects.get(board=post, id=comment_id).delete()

    post.save()
    return JsonResponse({'post_id': post_id, 'comment_id': comment_id})