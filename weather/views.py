from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import FormView

from dotenv import load_dotenv, find_dotenv
import os, requests

from .forms import ZipCodeForm

# Create your views here.

class indexForm(FormView):
    template_name = 'weather/index.html'
    form_class = ZipCodeForm

    def form_valid(self, form):
        zipcode = form.cleaned_data.get('zipcode')
        return redirect('weather:detail', zipcode)

def index(request):
    # return HttpResponse('/weather/')
    return render(request, 'weather/index.html')

def detail(request, **kwargs):
    zipcode = kwargs.get('zipcode', None)
    city = kwargs.get('city', None)
    state = kwargs.get('state', None)

    api_token = os.environ['WEATHER_KEY']
    if zipcode:
        payload = {
            'zip': f'{zipcode},us',
            'appid': api_token
        }
    elif city and state:
        payload = {
            'q': f'{city},us-{state}',
            'appid': api_token
        }
        print(payload)
    else:
        return HttpResponse('gotta provide something my man')
    res = requests.get('http://api.openweathermap.org/data/2.5/weather', payload) 
    parsed_res = str(res)
    status = res.json()
    return HttpResponse(f'{status}: {parsed_res}')