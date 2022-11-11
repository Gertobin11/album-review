from datetime import datetime, timezone
from django.db.models import Count
from reviews.models import Review, Genre


def number_of_reviews(user):
    """ Function to return the amount of reviews each user has """
    reviews = Review.objects.filter(creator=user)
    return len(reviews)


def days_since_joined(joined):
    """ Return the amount of days since the user joined """
    today = datetime.now(timezone.utc)
    return (today - joined).days


def reviews_per_genre(username):
    """
        Returns a queryset of the FK of the Genre and the amount of reviews
        the user has in the Genre
    """
    user_reviews = (Review.objects.filter(
                    creator=username).values(
                    'album__genre').annotate(review_count=Count('title')))
    return user_reviews


def get_genre_chart_data(user_reviews_by_genre):
    genres = [x.name for x in Genre.objects.all()]
    genres_reviewed = [0 for _ in range(len(Genre.objects.all()))]
    for genre_reviews in user_reviews_by_genre:
        list_index = genre_reviews['album__genre'] - 1
        genres_reviewed[list_index] = genre_reviews['review_count']

    return [genres, genres_reviewed]
