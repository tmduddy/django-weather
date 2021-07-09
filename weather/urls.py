from django.urls import path

from . import views

app_name='weather'
urlpatterns = [
    # /weather/
    path('', views.IndexForm.as_view(), name='index'),
    # /weather/<zip>/
    path('<int:zipcode>/', views.detail, name='detail'),
    # /weather/<city>/<state>/
    path('<str:city>/<str:state>/', views.detail, name='detail')
]
