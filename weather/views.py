from urllib.parse import urlencode

from django.http import Http404
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views.generic.edit import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.urls import reverse
from django.utils import timezone
import weather.helper as helper

from weather.models import Report

from weather.forms import CityStateSearchForm, ReportForm, ZipCodeSearchForm


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
        
        action = self.request.POST.get('action')

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
    template_name = 'weather/detail.html'

    def get(self, request, **kwargs):
        
        zipcode = kwargs.get('zipcode')
        city = kwargs.get('city')
        state = kwargs.get('state')
        
        payload = {}
        
        if zipcode:
            payload['zip'] = f'{zipcode},us'
        elif city and state:
            payload['q'] = f'{city},us-{state}'
        else:
            pass

        weather_data = helper.get_raw_weather_data(payload)
        weather_data_raw = weather_data.get('response')
        status = weather_data.get('status')
        
        if status not in [200, 201, 202]:
            error_text = f"Your call to the OpenWeatherMap API failed with a status of {status}"
            search_term = str(zipcode) if zipcode else f'{city}, {state}'
            context = {
                "error_text": error_text,
                "search_term": search_term
            }
            return render(request, 'weather/404.html', context)
        
        # map json response to readable output
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
        
        return render(request, self.template_name, context)

class ReportWeatherView(LoginRequiredMixin, View):
    template_name = 'weather/report-weather.html'
    login_url = 'account:login'

    def get(self, request):

        context = {
            'form': ReportForm
        }

        return render(request, self.template_name, context)

    def post(self, request):
        report_form = ReportForm(request.POST)
        
        # using the commit=False flag to hold off on sending the 
        # data to the db in case i need to add custom processing
        report_data = report_form.save(commit=False)
        
        # calling .save() here sends the record to the db
        report_data.save()


        # using a dict and urllib.urlencode to generate query strings
        # on redirect without defining them explictly in URLConf
        response = redirect('weather:browse_reports')
        params = {
            'pk': report_data.id
        }
        query_params = urlencode(params)

        response['Location'] += f'?{query_params}'

        return response

class BrowseReportsView(View):
    template_name = 'weather/browse-reports.html'

    def get(self, request):

        query_string_pk = request.GET.get('pk')
        query_string_today = request.GET.get('today')

        order_by_text = ['-report_date', 'state', 'city']
        
        if query_string_pk:
            all_reports = Report.objects.filter(pk=query_string_pk).order_by(*order_by_text)
        elif query_string_today:
            all_reports = Report.objects.filter(report_date__day=timezone.now().day).order_by(*order_by_text)
        else:
            all_reports = Report.objects.all().order_by(*order_by_text)[:10]

        fields = [str(field).replace('weather.Report.', '').upper() for field in Report._meta.fields if str(field) != "weather.Report.id"]
        context = {
            'all_reports': all_reports,
            'fields': fields,
        }
        return render(request, self.template_name, context)
