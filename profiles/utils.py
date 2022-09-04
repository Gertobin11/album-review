from reviews.models import Review


def number_of_reviews(user):
    """ Function to return the amount of reviews each user has """
    reviews = Review.objects.filter(creator=user)
    return len(reviews)
