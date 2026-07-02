from django.shortcuts import render
from .forms import PostForm
# Create your views here.
from .models import Post

def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'post.html', {'form': PostForm(), 'success': True})

    return render(request, 'post.html', {'form': PostForm()})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})