def average_rating(rating_list):
    """ Function to return the average rating of items """
    if not rating_list:
        return 0
    else:
        return round(sum(rating_list) / len(rating_list))