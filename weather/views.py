from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import FormView, View

from dotenv import load_dotenv, find_dotenv
import os, requests

from .forms import ZipCodeSearchForm, CityStateSearchForm

# Create your views here.

class IndexForm(View):
    template_name = 'weather/index.html'

    def get(self, request):
        zip_form = ZipCodeSearchForm(prefix='zip_form')
        city_state_form = CityStateSearchForm(prefix='city_state_form')

        return render(request, 'weather/index.html', {'zip_form': zip_form, 'city_state_form': city_state_form})
    
    def post(self, request):
        zip_form = ZipCodeSearchForm(prefix='zip_form')
        city_state_form = CityStateSearchForm(prefix='city_state_form')

        action = self.request.POST.get('action', False)

        if action == 'zip_form':
            zip_form = ZipCodeSearchForm(request.POST, prefix='zip_form')
            if zip_form.is_valid():
                zipcode = zip_form.cleaned_data['zipcode']
                return redirect('weather:detail', zipcode)
        elif action == 'city_state_form':
            city_state_form = CityStateSearchForm(request.POST, prefix='city_state_form')
            if city_state_form.is_valid():
                city = city_state_form.cleaned_data['city']
                state = city_state_form.cleaned_data['state']
                return redirect('weather:detail', city, state)

def detail(request, **kwargs):
    zipcode = kwargs.get('zipcode', None)
    city = kwargs.get('city', None)
    state = kwargs.get('state', None)

    api_token = os.environ['WEATHER_KEY']
    print(f'TOKEN {api_token}')
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