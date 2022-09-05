from .models import Profile
from .utils import number_of_reviews


def top_profiles(request):
    """ Return the profiles with most reviews """
    profiles = Profile.objects.all()
    profile_list = []
    for profile in profiles:
        profile_list.append({
            'profile': profile,
            'no_of_reviews': number_of_reviews(profile.user)
        })
    # Sort and get the 5 profiles with most views
    top_list = sorted(profile_list, key=lambda d: d['no_of_reviews'],
                      reverse=True)[:5]
    context = {
        'top_profiles': top_list
    }

    return context
