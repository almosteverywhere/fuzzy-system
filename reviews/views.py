from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SearchForm, ReviewForm
from .models import Review, Position
from datetime import datetime 
from django.urls import reverse
import re
from django.contrib.auth.decorators import login_required



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

        search_results = Review.objects.filter(position__job_title__icontains=job_title)\
                        .filter(position__company_name__icontains=company)\
                        .filter(position__location__icontains=location)

        context = {
                'search_results': search_results,
            }
        template = loader.get_template('reviews/search_results.html')

        # should this go to a url called search results instead? 
        return HttpResponse(template.render(context, request))

    return render(request, 'index.html', context={'form':form})


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    has_options = ['has_live_coding','has_pair_programming', 'has_take_home', 'can_meet_team', 'would_recommend'] 
    review_options = []
    for option in has_options:
        if getattr(review, option):
            option = re.sub("_", " ", option)
            option = re.sub("has", "", option)
            review_options.append(option)
    context = {'review': review, 'review_options': review_options }
    return render(request, 'reviews/review_detail.html', context)


def add_review(request):
    template = loader.get_template('reviews/add_review.html')
    context = {
        'form': ReviewForm(),
    }
    return HttpResponse(template.render(context, request))

@login_required
def post_review(request): 
    form = ReviewForm(request.POST)
    if form.is_valid():

        review = Review()

        # if position doesn't already exist create it 
        company = form.cleaned_data['company']
        location = form.cleaned_data['location']
        job_title = form.cleaned_data['job_title']

        position = Position.objects.get_or_create(company_name=company, location=location,job_title=job_title)

        # have to get first part of the tuple
        review.position = position[0] 
        review.rating = form.cleaned_data['rating']
        review.title = form.cleaned_data['title']
        review.comment = form.cleaned_data['comment']
        review.total_time = form.cleaned_data['total_time']
        review.total_number_interviews = form.cleaned_data['total_number_interviews']
        review.has_live_coding = form.cleaned_data['has_live_coding']
        review.has_pair_programming = form.cleaned_data['has_pair_programming']
        review.has_take_home = form.cleaned_data['has_take_home']
        review.can_meet_team = form.cleaned_data['can_meet_team']
        review.got_an_offer = form.cleaned_data['got_an_offer']
        review.would_recommend = form.cleaned_data['would_recommend']
        review.user_name = request.user.username
        review.pub_date = datetime.today()
        
        review.save()
       
        ###
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('review_detail', args=(review.id,)))


    return render(request, 'reviews/add_review.html', {form: ReviewForm()})
