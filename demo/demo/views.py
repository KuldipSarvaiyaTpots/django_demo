from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def homePage(request):
  # return HttpResponse("Hello world from home page")
  return render(request, "home.html")

def aboutPage(request):
  # return HttpResponse("about page")
  return render(request, "about.html")

def aboutPageMe(request):
  return HttpResponseRedirect("/about")