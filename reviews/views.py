from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import register
from reviews.models import Review, Album
from .utils import average_rating


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
        'reviews': reviews
    }
    template = 'review_list.html'
    return render(request, template, context)


def album_list(request):
    """
    Function to display a list of books with the average rating of those albums
    """
    albums = Album.objects.all()
    album_list = []
    for album in albums:
        reviews = album.review_set.all()
        if reviews:
            album_rating = average_rating([review.rating for
                                          review in reviews])
            number_of_reviews = len(reviews)
        else:
            album_rating = 0
            number_of_reviews = 0
        album_list.append({
            'album': album,
            'album_rating': album_rating,
            'number_of_reviews': number_of_reviews
        })
    context = {
        'album_list': album_list
        }
    template = 'album_list.html'
    return render(request, template, context)


def album_view(request, id):
    """ Display individual reviews"""
    album = get_object_or_404(Album, pk=id)
    reviews = album.review_set.all()
    context = {
        'album': album,
        'reviews': reviews
    }
    template = 'album_view.html'
    return render(request, template, context)


def review(request, id):
    """ Display an individual review """
    review = get_object_or_404(Review, pk=id)
    context = {
        'review': review
    }
    template = 'review.html'
    return render(request, template, context)


@register.filter
def get_range(value):
    """ Returns a range from an integer in jinja 2 templating """
    return range(value)
