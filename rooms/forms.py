from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):
    city = forms.CharField(required=False)
    country = CountryField().formfield()
    amenity = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
