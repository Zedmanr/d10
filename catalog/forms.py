from django import forms
from catalog.models import TRANSMISSION_TYPE


class CarForm(forms.Form):
    manufacturer = forms.CharField(max_length=30)
    model_of_auto = forms.CharField(max_length=40)
    year_of_issue = forms.IntegerField()
    transmission = forms.IntegerField(widget=forms.RadioSelect(choices=TRANSMISSION_TYPE))
    colour = forms.CharField(max_length=20)