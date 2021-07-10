from django.forms import forms, CharField, TextInput, ModelForm
from .models import Report

class ZipCodeSearchForm(forms.Form):
    zipcode = CharField(label="Zipcode", max_length=5, widget=TextInput(attrs={'placeholder': 'ex. 20002'}))

class CityStateSearchForm(forms.Form):
    city = CharField(max_length=200, widget=TextInput(attrs={'placeholder': 'ex. Annapolis'}))
    state = CharField(label="State Code", max_length=2, widget=TextInput(attrs={'placeholder': 'ex. MD'}))

class ReportForm(ModelForm):
    description = CharField(
        max_length=500,
        required=False
    )

    class Meta:
        model = Report
        fields = [
            'city',
            'state',
            'zipcode',
            'temperature',
            'weather',
            'description',
        ]