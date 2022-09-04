from django.contrib import messages


def average_rating(rating_list):
    """ Function to return the average rating of items """
    if not rating_list:
        return 0
    else:
        return round(sum(rating_list) / len(rating_list))


def attach_album_attributes(albums, album_list):
    """ Attach the ratings and number of reviews to any custom album list """
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
    return album_list


def user_message(request, type, field):
    """ Add a level type message and get the name from the field """
    name = request.POST.get(field)
    if type == 'success':
        return messages.success(request, f'{name} has been added !')
    elif type == 'error':
        return messages.error(request, 'Something went wrong,'
                              'please try again')
