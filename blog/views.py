from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.http import HttpResponseNotFound
def post_search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            posts = get_list_or_404(Post.objects.filter(title__icontains=search))
            return render(request, 'blog/post_list.html', {'posts': posts})
            print("Entro aqui")

def post_list(request):
    posts = get_list_or_404(Post.objects.all())
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk).delete()
    posts = get_list_or_404(Post.objects.all())
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})