from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

from .forms import PostView, CommentView
from .models import Post, Comment

def HomeView(request):
    objects = Post.objects.all().order_by('-create_date_post')
    paginator = Paginator(objects, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home/index.html', {'page': page, 'posts': posts})

def Post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentView(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.comment_author = request.user
            new_comment.save()
            return redirect('post_detail', post.id)
    else:
        comment_form = CommentView()
    return render(request,'post/detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
@login_required
def Post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostView(instance=post , data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post.id)
    else:
        form = PostView(instance=post)
    return render(request, 'post/edit.html', {'form': form, 'post': post})

@login_required
def Post_create(request):
    if request.method == 'POST':
        form = PostView(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author_post = request.user
            post.create_date_post = timezone.now()
            post.save()
            return redirect('post_detail', post.id)
    else:
        form = PostView(request.POST)
    return render(request, 'post/create.html', {'form': form})

@login_required
def Comment_delete(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('HomeView')

@login_required
def Post_delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("/")
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")
        
def SportView(request):
    objects = Post.objects.filter(category_post='sport').order_by('-create_date_post')
    paginator = Paginator(objects, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home/index.html', {'page': page, 'posts': posts})

def ScienceView(request):
    objects = Post.objects.filter(category_post='science').order_by('-create_date_post')
    paginator = Paginator(objects, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home/index.html', {'page': page, 'posts': posts})

def EconomicsView(request):
    objects = Post.objects.filter(category_post='economics').order_by('-create_date_post')
    paginator = Paginator(objects, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home/index.html', {'page': page, 'posts': posts})

def OtherView(request):
    objects = Post.objects.filter(category_post='').order_by('-create_date_post')
    paginator = Paginator(objects, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home/index.html', {'page': page, 'posts': posts})