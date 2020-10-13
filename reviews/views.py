from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SearchForm
from .models import Review

# Create your views here.

# first page with the search form 
def index(request):
    template = loader.get_template('index.html')
    context = {
        'form': SearchForm(),
    }
    return HttpResponse(template.render(context, request))
   
def search(request):

    form = SearchForm(request.POST)
    if form.is_valid():
        company = form.cleaned_data['company']
        job_title = form.cleaned_data['job_title']
        location = form.cleaned_data['location']

        import pdb; pdb.set_trace()
        search_results = Review.objects.filter(position__job_title__icontains=job_title)\
                        .filter(position__company_name__icontains=company)\
                        .filter(position__location__icontains=location)

        context = {
                'search_results': search_results,
            }
        template = loader.get_template('reviews/search_results.html')

        return HttpResponse(template.render(context, request))

    return render(request, 'index.html', context={'form':form})


    # should a review have a position? 

    # what about if we do company has a position has a review
    # and position has a location also 
    #         search_results = Reviews.objects.filter(interview__location__icontains=location).filter(interview__company__name__icontains=company).filter(interview__position__icontains=jobtitle)
    # all reviews that have a company name of ....
    # all reviews that have a position of ...., but the position should be one position object
    # all reviews that have a position of title, company name, location
    # should the position object be unique? 
    # should it be positions have companys and reviews? 
    # or should it be companies should have positions and positions should bave reviews?
    # that's more the real world way but maybe this is better? 
    # review.position.company would be ideal
    # urls wil lbe like /reviews/1234, shouldn't have to specify company 
    # well let's try it and we can see otherwise
    # Reviews.objects.filter(position__jobtitle)
    # should it be like reviews.position.company
    # or review.position and review.company
    # position should be like software engineer at facebook, menlo park
    # then it has reviews. should company even be a 
    # position has reviews, position has company name, location, and reviews
    # one position has multiple reviews. 
    