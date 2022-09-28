from datetime import datetime, timezone
from reviews.models import Review


def number_of_reviews(user):
    """ Function to return the amount of reviews each user has """
    reviews = Review.objects.filter(creator=user)
    return len(reviews)


def days_since_joined(joined):
    """ Return the amount of days since the user joined """
    today = datetime.now(timezone.utc)
    return (today - joined).days
