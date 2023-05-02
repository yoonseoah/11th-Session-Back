from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from community.models import Posting

# Create your views here.

def List(request):
    posts = Posting.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    return render(request, 'detail.html', {'post':post})

def search(request):
    context = dict()
    #free_post = Posting.objects.filter(category__icontains="🦁아기사자 대나무숲🎋").order_by('-id')
    free_post = Posting.objects.filter(category__icontains=Posting).order_by('-id')
    post = request.POST.get('post',"")
    if post:
        free_post = free_post.filter(title__icontains=post)
        context['free_post'] = free_post
        context['post'] = post
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')