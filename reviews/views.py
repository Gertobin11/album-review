from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaulttags import register
from reviews.models import Review, Album
from .utils import attach_album_attributes
from .forms import (GenreForm, SearchForm, ArtistForm,
                    RecordCompanyForm, AlbumForm)


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
    attach_album_attributes(albums, album_list)
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


def search(request):
    """ Display the search results to the user """

    form = SearchForm(request.GET)
    search_term = request.GET.get('search', '')
    album_list = []
    search_count = 0
    search_category = ''
    if form.is_valid() and form.cleaned_data['search']:
        search = form.cleaned_data['search']
        search_results = Album.objects.filter(title__icontains=search)
        if form.cleaned_data['search_in']:
            search_category = form.cleaned_data['search_in']
            print(search_category)
            if search_category == 'group':
                search_results = Album.objects.filter(artist__name__icontains=search)
            elif search_category == 'title':
                search_results = Album.objects.filter(title__icontains=search)
            elif search_category == 'reviewer':
                search_results = Album.objects.filter(review__creator__username__icontains=search)
        search_count = len(search_results)
        attach_album_attributes(search_results, album_list)
    else:
        print(form.errors)
    template = 'search_results.html'

    context = {
        'album_list': album_list,
        'search_term': search_term,
        'search_count': search_count,
        'search_category': search_category
    }

    return render(request, template, context)


def advanced_sarch(request):
    """ View to render an advanced search form """
    form = SearchForm()
    template = 'advanced_search.html'
    context = {
        'form': form
    }
    return render(request, template, context)


def add_review(request):
    """ Allow a user to upload a review """
    artist_form = ArtistForm()
    genre_form = GenreForm()
    recored_company_form = RecordCompanyForm()
    album_form = AlbumForm()
    template = 'add_review.html'
    context = {
        'artist_form': artist_form,
        'genre_form': genre_form,
        'record_company_form': recored_company_form,
        'album_form': album_form
    }

    return render(request, template, context)


def add_artist(request):
    """ Allows a user to add info about an artist """
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add_review')


def add_genre(request):
    """ Allows the user to add a genre """
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add_review')


def add_record_label(request):
    """ Allows the user to add a record label """
    if request.method == 'POST':
        form = RecordCompanyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add_review')


def add_album(request):
    """ Allows the user to add an album """
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
        else:
            print(form.errors)
        return redirect('add_review')


@register.filter
def get_range(value):
    """ Returns a range from an integer in jinja 2 templating """
    return range(value)
