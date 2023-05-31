from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, HashTag, Comment
from django.utils import timezone 
from .forms import Blogform, CommentForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)
    blog_hashtag = blog_detail.hashtag.all()
    return render(request, 'detail.html', {'blog':blog_detail, 'hashtags':blog_hashtag})

def new(request):
    form = Blogform()
    return render(request, 'new.html', {'form':form})

def create(request):
    form = Blogform(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.date = timezone.now()
        new_blog.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_blog.hashtag.add(new_hashtag[0])
        return redirect('detail', new_blog.id)
    return redirect('home')

def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, pk=blog_id)
    blog_delete.delete()
    return redirect('home')

def update_page(request, blog_id):
    blog_update = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'update.html', {'blog':blog_update})

def update(request, blog_id):
    blog_update = get_object_or_404(Blog, pk=blog_id)
    blog_update.title = request.POST['title']
    blog_update.body = request.POST['body']
    blog_update.save()
    return redirect('home')

def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.save()
            return redirect('detail', blog_id)

    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form' : form}
    )


        