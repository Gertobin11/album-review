from datetime import datetime, timezone
from django.db.models import Count
from reviews.models import Review


def number_of_reviews(user):
    """ Function to return the amount of reviews each user has """
    reviews = Review.objects.filter(creator=user)
    return len(reviews)


def days_since_joined(joined):
    """ Return the amount of days since the user joined """
    today = datetime.now(timezone.utc)
    return (today - joined).days


def reviews_per_genre(username):
    user_reviews = (Review.objects.filter(
                    creator=username).values(
                    'album__genre').annotate(review_count=Count('title')))
    return user_reviews
