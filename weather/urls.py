from django.urls import path

from . import views

app_name='weather'

urlpatterns = [
    # /weather/
    path('', views.IndexView.as_view(), name='index'),
    # /weather/search/
    path('search/', views.SearchForm.as_view(), name='search'),
    # /weather/search/<zip>/
    path('search/<int:zipcode>/', views.DetailView.as_view(), name='detail'),
    # /weather/search/<city>/<state>/
    path('search/<str:city>/<str:state>/', views.DetailView.as_view(), name='detail'),
    # /weather/report-weather/
    path('report-weather/', views.ReportWeatherView.as_view(), name='report_weather'),
    # /weather/browse-reports/
    path('browse_reports', views.BrowseReportsView.as_view(), name='browse_reports')
]
