from django import views
from django.urls import path

from . import views

urlpatterns = [
   path('login/', views.LoginForm.as_view(), name="login"),
   path("logout/", views.Logout.as_view(), name="logout"),
   path("signup/", views.Signup.as_view(), name="signup"),
]
