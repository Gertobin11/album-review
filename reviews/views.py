from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
from reviews.models import Review, Album
from .utils import attach_album_attributes, user_message, check_user_is_creator
from .forms import (GenreForm, SearchForm, ArtistForm,
                    RecordCompanyForm, AlbumForm, ReviewForm)


def index(request):
    """ Function to render the landing page view """
    template = 'index.html'
    return render(request, template)


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
    reviews = Review.objects.all().order_by("-date_created_on")
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
    # Insert the albums viewed into local storage
    if request.user.is_authenticated:
        viewed_albums = request.session.get('viewed_albums', [])
        viewed_album = [album.id, album.title]
        if viewed_album in viewed_albums:
            viewed_albums.remove(viewed_album)
        viewed_albums.insert(0, viewed_album)
        viewed_albums = viewed_albums[:5]
        request.session['viewed_albums'] = viewed_albums
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
            if search_category == 'group':
                search_results = (Album.objects.filter(
                                  artist__name__icontains=search))
            elif search_category == 'album':
                search_results = Album.objects.filter(title__icontains=search)
            else:
                search_results = (Album.objects.filter(
                                  review__creator__username__icontains=search))
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


@login_required
def add_review(request):
    """ Allow a user to upload a review """
    artist_form = ArtistForm()
    genre_form = GenreForm()
    recored_company_form = RecordCompanyForm()
    album_form = AlbumForm()
    review_form = ReviewForm()
    template = 'add_review.html'
    context = {
        'artist_form': artist_form,
        'genre_form': genre_form,
        'record_company_form': recored_company_form,
        'album_form': album_form,
        'review_form': review_form
    }
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            valid_form = form.save(commit=False)
            valid_form.creator = request.user
            valid_form.save()
            user_message(request, 'success', 'title')
            return redirect('review_list')
        else:
            print(form.errors)
            user_message(request, 'error', 'title')

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    """ View to allow users to edit their own reviews """
    initial_form = get_object_or_404(Review, pk=review_id)
    if not check_user_is_creator(request.user.id, initial_form.creator.id):
        if request.user.is_superuser:
            pass
        else:
            user_message(request, 'permission_denied', 'title')
            return redirect('home')
    review_form = ReviewForm(instance=initial_form)
    template = 'edit_review.html'
    context = {
        'initial_form': initial_form,
        'review_form': review_form
    }
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST, instance=initial_form)
        if review_form.is_valid():
            review_form.save()
            return redirect('review', initial_form.id)
        else:
            user_message(request, 'error', 'title')
    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Allow User or superuser to delete a review """
    review = get_object_or_404(Review, pk=review_id)
    if not check_user_is_creator(request.user.id, review.creator.id):
        if request.user.is_superuser:
            pass
        else:
            user_message(request, 'permission_denied', 'title')
            return redirect('home')
    user_message(request, 'deleted', review)
    review.delete()
    return redirect('review_list')


@login_required
def add_artist(request):
    """ Allows a user to add info about an artist """
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            user_message(request, 'success', 'name')
        return redirect('add_review')


@login_required
def add_genre(request):
    """ Allows the user to add a genre """
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            user_message(request, 'success', 'name')
        return redirect('add_review')


@login_required
def add_record_label(request):
    """ Allows the user to add a record label """
    if request.method == 'POST':
        form = RecordCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            user_message(request, 'success', 'name')
        return redirect('add_review')


@login_required
def add_album(request):
    """ Allows the user to add an album """
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user_message(request, 'success', 'title')
        else:
            print(form.errors)
        return redirect('add_review')


@register.filter
def get_range(value):
    """ Returns a range from an integer in jinja 2 templating """
    return range(value)
