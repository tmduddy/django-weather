from django.forms import forms

class ZipCodeForm(forms.Form):
    zipcode = forms.Field()