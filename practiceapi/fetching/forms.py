# forms.py

from django import forms

class EndpointForm(forms.Form):
    endpoint = forms.CharField(label='API Endpoint', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter API endpoint(s)', 'class': 'form-control'}))
    headlines = forms.ChoiceField(label='Headlines', choices=[('top-headlines', 'Top Headlines'), ('everything', 'Everything')], widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    country = forms.CharField(label='Country', max_length=2, widget=forms.TextInput(attrs={'placeholder': 'Enter country code (e.g., us)', 'class': 'form-control'}))
    source = forms.CharField(label='Source', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter source name', 'class': 'form-control'}))
    category = forms.CharField(label='Category', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter category name', 'class': 'form-control'}))
    