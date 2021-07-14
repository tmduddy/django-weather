from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='account'

urlpatterns = [
  
  # /account/login
  path('login/', auth_views.LoginView.as_view(), name='login'),
  # # /account/logout
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  # # /account/register
  # path('register/', views.RegisterView.as_view(), name='register'),    
]
