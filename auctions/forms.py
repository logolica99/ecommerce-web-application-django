from django.forms import ModelForm
from .models import *
from django import forms
class ListingForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 7}))
    class Meta:
        model = Listing
        fields='__all__'

class WatchlistForm(ModelForm):
    class Meta:
        model = watchlist
        fields="__all__"
