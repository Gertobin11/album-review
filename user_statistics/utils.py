from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from reviews.views import Review, Album
from django.db.models import Count


def get_data_lists(type):
    """
        Return 2 lists with the name of each album and
        their corresponding number of reviews
    """
    if type == 'reviews_per_album':
        count_of_objects = (Review.objects.all().values(
                        'album').annotate(count=Count('title')))
        objects = [get_object_or_404(Album, pk=x['album']).title
                   for x in count_of_objects]

    elif type == 'reviews_per_user':
        count_of_objects = (Review.objects.all().values(
                        'creator').annotate(count=Count('title')))
        objects = [get_object_or_404(User, pk=x['creator']).username
                   for x in count_of_objects]

    reviews = [x['count'] for x in count_of_objects]
    return objects, reviews
