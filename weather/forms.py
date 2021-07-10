from django.forms import forms, CharField, TextInput

class ZipCodeSearchForm(forms.Form):
    zipcode = CharField(label="Zipcode", max_length=5, widget=TextInput(attrs={'placeholder': 'ex. 20002'}))

class CityStateSearchForm(forms.Form):
    city = CharField(max_length=200, widget=TextInput(attrs={'placeholder': 'ex. Annapolis'}))
    state = CharField(label="State Code", max_length=2, widget=TextInput(attrs={'placeholder': 'ex. MD'}))