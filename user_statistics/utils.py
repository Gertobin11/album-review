from django.shortcuts import get_object_or_404
from reviews.views import Review, Album
from django.db.models import Count


def get_lists_of_albums_and_no_of_reviews():
    """
        Return 2 lists with the name of each album and
        their corresponding number of reviews
    """
    no_of_reviews = (Review.objects.all().values(
                    'album').annotate(review_count=Count('title')))
    albums = [get_object_or_404(Album, pk=x['album']).title
              for x in no_of_reviews]
    reviews = [x['review_count'] for x in no_of_reviews]
    return albums, reviews
