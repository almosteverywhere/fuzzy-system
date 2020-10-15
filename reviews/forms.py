from django import forms
from .models import Review

class SearchForm(forms.Form):
    company = forms.CharField(label='Company', max_length=100)
    job_title = forms.CharField(label='Job title', max_length=100)
    location = forms.CharField(label='Location', max_length=100)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['position', 'pub_date', 'user_name']

    company = forms.CharField(
        label="Company",
        max_length=70,
        widget=forms.TextInput(),
        required=True,
    )
    job_title = forms.CharField(
        label="Job title",
        max_length=90,
        widget=forms.TextInput(),
        required=True,
    )

    location = forms.CharField(
        label="Location",
        max_length=90,
        widget=forms.TextInput(),
        required=True,
    )

    field_order = ['company', 'job_title', 'location']



    
       