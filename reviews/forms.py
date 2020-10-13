from django import forms

class SearchForm(forms.Form):
    company = forms.CharField(label='Company', max_length=100)
    job_title = forms.CharField(label='Job title', max_length=100)
    location = forms.CharField(label='Location', max_length=100)
