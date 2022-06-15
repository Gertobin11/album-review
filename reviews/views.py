from django.shortcuts import render
from reviews.models import Review

def index(request):
    """ Function to render the landing page view """
    name = request.GET.get('name') or "world"
    context = {
        'name': name
    }
    template = 'index.html'
    return render(request, template, context)

def search_results(request):
    """ Function to render the results of the users search query """
    if request.method == 'POST':
        return
    else:
        context = {}
        template = 'search_results.html'
        return render(request, template, context)

def review_list(request):
    """ Function to display the list of reviews left by users """
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews
    }
    template = 'review_list.html'
    return render(request, template, context)