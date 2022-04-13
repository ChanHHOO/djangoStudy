# Create your views here.

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
from . import models
from django.contrib.auth.decorators import login_required

Post = models.Post.objects.all()

context = {
    'posts': Post
}
cc = {
    'sdd': "asd",
}

def index(request):
    
    posts = models.Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'posts/index.html', context)


def detail(request, post_id):
    post = models.Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    print(post.image)
    return render(request, 'posts/detail.html', context)

@login_required
def new(request):
    return render(request, 'posts/new.html')

@login_required
def create(request):
    user = request.user
    body = request.POST.get('body')
    image = request.FILES.get('image')
    post = models.Post(user=user,image=image, body=body, created_at=timezone.now())
    post.save()
    return redirect('posts:detail', post_id=post.id)

@login_required
def edit(request, post_id):
    try:
        post = models.Post.objects.get(id=post_id, user=request.user)
    except models.Post.DoesNotExist:
        return redirect('posts:index')
    context = {
        'post' : post,
    }
    post.save()
    return render(request, 'posts/edit.html', context)
@login_required 
def update(request, post_id):
    try:
        post = models.Post.objects.get(id=post_id, user=request.user)
    except models.Post.DoesNotExist:
        return redirect('posts:index')
    post.body = request.POST.get('body')
    image = request.FILES.get('image')
    if image:
        post.image = image
    post.save()
    return redirect('posts:detail', post_id=post.id)

@login_required
def delete(request, post_id):
    try:
        post = models.Post.objects.get(id=post_id, user=request.user)
    except models.Post.DoesNotExist:
        return redirect('posts:index')
    post.delete()
    return redirect('posts:index')

@login_required
def like(request, post_id):
    try:
        post = models.Post.objects.get(id=post_id)
        if request.user in post.liked_users.all():
            post.liked_users.remove(request.user)
        else:
            post.liked_users.add(request.user)
        return redirect('posts:detail', post_id=post.id)
    except Post.DoesNotExist:
        pass
    return redirect('posts:index')