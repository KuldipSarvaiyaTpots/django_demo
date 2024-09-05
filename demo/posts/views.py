from django.shortcuts import render
from .models import posts

# Create your views here.
def showPosts(request):
  post = posts.objects.all().order_by("-created_at")
  return render(request, 'posts.html', {"posts": post})

def showSinglePost(request, id):
  post = posts.objects.get(id=id)
  return render(request, 'post.html', {"post": post})