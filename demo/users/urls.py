from django.urls import path
from .views import registrationForm, loginForm, logoutBtn

urlpatterns = [
    path('registration/', registrationForm, name="users-registration"),
    path('login/', loginForm, name="users-login"),
    path('logout/', logoutBtn, name="users-logout"),
]
