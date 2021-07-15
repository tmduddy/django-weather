from django.urls import path
from django.contrib.auth import views as auth_views

from account import views

app_name='account'

urlpatterns = [
  
  # /account/login
  path('login/', auth_views.LoginView.as_view(), name='login'),
  # # /account/logout
  path('logout/', views.LogoutView.as_view(), name='logout'),
  # # /account/register
  # path('register/', views.RegisterView.as_view(), name='register'),    
]
