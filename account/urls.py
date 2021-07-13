from django.urls import path

from . import views

app_name='account'

urlpatterns = [

  # /account/login
  # path('login/', views.user_login, name='login'),
  # /account/logout
  # path('logout/', views.LogoutView.as_view(), name='logout'),
  # # /account/register
  # path('register/', views.RegisterView.as_view(), name='register'),

  # CBV approach
  # /account/login
  path('login/', views.LoginView.as_view(), name='login'),
  # # /account/logout
  # path('logout/', views.LogoutView.as_view(), name='logout'),
  # # /account/register
  # path('register/', views.RegisterView.as_view(), name='register'),    
]
