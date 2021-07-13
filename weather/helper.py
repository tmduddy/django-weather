import os
from random import randint, random
from math import floor
import requests

from weather.models import Report


def get_raw_weather_data(payload: dict):

  api_token = os.environ['WEATHER_KEY']

  payload['appid'] = api_token
  payload['units'] = 'imperial'
  
  res = requests.get('http://api.openweathermap.org/data/2.5/weather', payload) 
  
  status = res.status_code

  return {'response': res.json(), 'status': status}

def populate_report_table(num_entries: int):

  reports = []

  while len(reports) < num_entries:
    zipcode = str(floor(100000 * random()))
  
    payload = {
      'zip': str(zipcode)
    }

    weather_data = get_raw_weather_data(payload)
    weather_data_raw = weather_data['response'] if weather_data['status'] in [200, 201, 202] else None

    if weather_data_raw:
      print(f'Generating weather object: {len(reports)+1} / {num_entries}')
      # map json response to readable output
      city = weather_data_raw.get('name', 'unknown')
      all_weather = weather_data_raw.get('weather', [{}])[0]
      weather = all_weather.get('main', 'unknown')
      description = all_weather.get('description', 'unknown')
      all_temps = weather_data_raw.get('main', {})
      current_temp = all_temps.get('temp', 'unknown')
      
      weather_data = {
        'city': city,
        'state': 'US',
        'zipcode': zipcode,
        'weather': weather,
        'description': description,
        'temperature': current_temp,
      }
      reports.append(weather_data)
  for i, report in enumerate(reports):
    print(f'Loading object to DB: {i+1} / {num_entries}')
    Report.objects.create(**report)
