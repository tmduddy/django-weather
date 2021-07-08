from django.shortcuts import render
from django.http import HttpResponse

from dotenv import load_dotenv, find_dotenv
import os, requests

# Create your views here.
def index(request):
    return HttpResponse('/weather/')

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