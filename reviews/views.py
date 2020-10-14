from django.shortcuts import render, get_object_or_404
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

        search_results = Review.objects.filter(position__job_title__icontains=job_title)\
                        .filter(position__company_name__icontains=company)\
                        .filter(position__location__icontains=location)

        context = {
                'search_results': search_results,
            }
        template = loader.get_template('reviews/search_results.html')

        return HttpResponse(template.render(context, request))

    return render(request, 'index.html', context={'form':form})


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    context = {'review': review}
    return render(request, 'reviews/review_detail.html', context)
