import os

import requests
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic.edit import View

from .forms import CityStateSearchForm, ZipCodeSearchForm


class IndexView(View):
    template_name = 'weather/index.html'

    def get(self, request):
        context = {}
        return render(request, 'weather/index.html', context)

class SearchForm(View):
    template_name = 'weather/search.html'

    def get(self, request):
        zip_form = ZipCodeSearchForm(prefix='zip_form')
        city_state_form = CityStateSearchForm(prefix='city_state_form')
        context = {
            'zip_form': zip_form,
            'city_state_form': city_state_form,
        }
        return render(request, 'weather/search.html', context)
    
    def post(self, request):
        
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

class DetailView(View):

    def get(self, request, **kwargs):
        zipcode = kwargs.get('zipcode', None)
        city = kwargs.get('city', None)
        state = kwargs.get('state', None)

        api_token = os.environ['WEATHER_KEY']
        
        payload = {
            'appid': api_token,
            'units': 'imperial',
        }
        
        if zipcode:
            payload['zip'] = f'{zipcode},us'
        elif city and state:
            payload['q'] = f'{city},us-{state}'
        else:
            pass

        res = requests.get('http://api.openweathermap.org/data/2.5/weather', payload) 
        status = res.status_code
        
        if status not in [200, 201, 202]:
            error_text = f"Your call to the OpenWeatherMap API failed with a status of {status}"
            return Http404(error_text)
        
        # map json response to readable output
        weather_data_raw = res.json()
        city = weather_data_raw.get('name', 'unknown')
        all_weather = weather_data_raw.get('weather', [{}])[0]
        weather = all_weather.get('main', 'unknown')
        description = all_weather.get('description', 'unknown')
        all_temps = weather_data_raw.get('main', {})
        current_temp = all_temps.get('temp', 'unknown')
        feel_temp = all_temps.get('feels_like', 'unknown')
        high_temp = all_temps.get('temp_max', 'unknown')
        low_temp = all_temps.get('temp_min', 'unknown')
        
        weather_data = {
            'city': city,
            'weather': weather,
            'description': description,
            'current_temp': current_temp,
            'feels_temp': feel_temp,
            'high_temp': high_temp,
            'low_temp': low_temp,
        }

        header_list = [header.replace('_temp', '').title() for header in weather_data]
        
        context = {
            'weather_data': weather_data,
            'header_list': header_list
        }
        
        return render(request, 'weather/detail.html', context)
