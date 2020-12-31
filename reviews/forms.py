from django import forms
from .models import Review

    
CHOICES=[
        (True,'Yes'),
         (False,'No'),
         ]


class SearchResultsForm(forms.Form):
    company = forms.CharField(label='Company', max_length=100, required=False)
    job_title = forms.CharField(label='Job title', max_length=100, required=False)
    location = forms.CharField(label='Location', max_length=100, required=False)
    # this should be by buckets 
    total_time = forms.IntegerField(required=False)
    # this should also be by buckets
    total_number_interviews = forms.IntegerField(required=False)
    # they should allow searching by yes/no/don't care 
    has_live_coding = forms.ChoiceField(required=False, label="Has live coding", choices=CHOICES)
    has_pair_programming = forms.BooleanField(required=False)
    has_take_home = forms.BooleanField(required=False)
    can_meet_team = forms.BooleanField(required=False)
    got_an_offer = forms.BooleanField(required=False)
    would_recommend = forms.BooleanField(required=False)

    # rating = forms.IntegerField(choices=RATING_CHOICES, help_text="rating from 1 to 5")
    # self.fields['msp_host'].widget = HiddenInput()
    # can this just be set above? do we only need this in meta if it's a subclass?
    def __init__(self, *args, **kwargs):
        super(SearchResultsForm, self).__init__(*args, **kwargs)
        self.fields['company'].widget = forms.HiddenInput()
        self.fields['job_title'].widget = forms.HiddenInput()
        self.fields['location'].widget = forms.HiddenInput()
        # OK THIS IS FUCKED HOW TO SET A DEFAULT OPTION BC IF YOU SUBMIT THE Form
        # WITH NOTHING IT CONSIDERS IT FALSE BY DEFALUT 
        self.fields['has_live_coding'].widget = forms.RadioSelect(choices=CHOICES)
        self.fields['has_pair_programming'].widget = forms.RadioSelect(choices=CHOICES)

class EntrySearchForm(forms.Form):

    # class Meta:
    #     exclude = ['position', 'company', 'location']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    company = forms.CharField(label='Company', max_length=100, required=False)
    job_title = forms.CharField(label='Job title', max_length=100, required=False)
    location = forms.CharField(label='Location', max_length=100, required=False)


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


class ReviewFilterForm(forms.Form):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    
    


    
       