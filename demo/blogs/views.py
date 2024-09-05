from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def allBlogs(requst):
  return render(requst, "blogs.html")
  # data = [{'title': "blog.title", 'content': "blog.content"}]
  # return JsonResponse(data, safe=False)