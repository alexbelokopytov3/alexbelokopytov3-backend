from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import PostView
from .models import Post

# Create your views here.


def HomeView(request):
    objects = Post.objects.all().order_by('-create_date_post')
    paginator = Paginator(objects, 3)
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
    return render(request,'post/detail.html', {'post': post})

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
    return render(request, 'post/edit.html', {'form': form})

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