from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls')),
    path('account/', include('account.urls')),
]
