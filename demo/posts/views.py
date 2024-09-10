from django.shortcuts import render, redirect
from .models import Posts
from django.contrib.auth.decorators import login_required
from .forms import CreatPosts

# Create your views here.
def showPosts(request):
  post = Posts.objects.all().order_by("-created_at")
  return render(request, 'posts.html', {"posts": post})

def showSinglePost(request, id):
  post = Posts.objects.get(id=id)
  return render(request, 'post.html', {"post": post})

@login_required(login_url="/users/login")
def newPost(request):
  if request.method == "POST":
    form = CreatPosts(request.POST, request.FILES)
    if form.is_valid():
      new_post = form.save(commit=False)
      new_post.author = request.user
      new_post.save()
      return redirect("/posts")
  else:
    form = CreatPosts()
  return render(request, 'new_post.html', {"form": form})