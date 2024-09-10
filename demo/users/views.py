from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def registrationForm(request):
  if(request.method == "POST"):
    form = UserCreationForm(request.POST)
    if form.is_valid():
      login(request, form.save())
      return redirect("/admin")
  else: 
    form = UserCreationForm()

  return render(request, 'registrationForm.html', {"form": form})

def loginForm(request):
  if(request.method == "POST"):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      login(request, form.get_user())
      if 'redirect' in request.POST:
        return redirect(request.POST.get('redirect'))
      return redirect("/admin")
  else:
    form = AuthenticationForm()
  
  return render(request, 'login.html', {"form": form})

def logoutBtn(request):
  if request.method == "POST":
    logout(request)
    return redirect("/")