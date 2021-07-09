from django.forms import forms, CharField

class ZipCodeSearchForm(forms.Form):
    zipcode = CharField(label="Zipcode", max_length=5)

class CityStateSearchForm(forms.Form):
    city = CharField(max_length=200)
    state = CharField(label="Two Character State Code", max_length=2)