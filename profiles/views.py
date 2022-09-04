from django.shortcuts import render
from .models import Profile
from .utils import number_of_reviews


def profiles(request):
    """ Return all created profiles"""
    profiles = Profile.objects.all()
    profile_list = []
    for profile in profiles:
        # Attach the number of reviews each user has
        profile_list.append({
            'profile': profile,
            'no_of_reviews': number_of_reviews(profile.user)
        })
    template = 'profiles.html'
    context = {
        'profile_list': profile_list,
    }
    return render(request, template, context)
