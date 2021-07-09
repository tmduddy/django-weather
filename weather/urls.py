from django.urls import path

from . import views

app_name='weather'
urlpatterns = [
    # /weather/
    path('', views.IndexView.as_view(), name='index'),
    # /weather/search/
    path('search/', views.SearchForm.as_view(), name='search'),
    # /weather/search/<zip>/
    path('search/<int:zipcode>/', views.detail, name='detail'),
    # /weather/search/<city>/<state>/
    path('search/<str:city>/<str:state>/', views.detail, name='detail')
]
