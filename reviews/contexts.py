from .models import Review


def latest_reviews(request):
    """ Return the 5 latest reviews """
    reviews = Review.objects.all()
    sorted_reviews = sorted(reviews, key=lambda x: x.date_created_on,
                            reverse=True)[:5]
    context = {
        'latest_reviews': sorted_reviews
    }
    print(sorted_reviews)
    return context
