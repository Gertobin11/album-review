from django.shortcuts import render, get_object_or_404
from .models import Profile
from .utils import number_of_reviews
from .forms import EditProfileForm


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


def user_profile(request, profile_id):
    """ Return a single user profile """
    profile = get_object_or_404(Profile, pk=profile_id)
    no_of_reviews = number_of_reviews(profile.user)
    profile_form = EditProfileForm(instance=profile)
    context = {
        'profile': profile,
        'no_of_reviews': no_of_reviews,
        'profile_form': profile_form
    }
    template = 'user_profile.html'
    return render(request, template, context)
