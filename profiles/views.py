from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib import messages
from .models import Profile
from .utils import number_of_reviews, days_since_joined
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
    recently_viewed = request.session.get('viewed_albums', [])
    days_joined = days_since_joined(profile.created_on)
    time_since_joined = naturaltime(profile.created_on)
    no_of_reviews = number_of_reviews(profile.user)
    profile_form = EditProfileForm(instance=profile)
    follows = list(profile.user.followed.all())
    print(follows)
    for person in profile.followers.all():
        print(person)
    context = {
        'profile': profile,
        'no_of_reviews': no_of_reviews,
        'profile_form': profile_form,
        'days_joined': days_joined,
        'time_since_joined': time_since_joined,
        'recently_viewed': recently_viewed,
        'follows': follows
    }
    template = 'user_profile.html'
    return render(request, template, context)


def followers(request, user_id):
    """ Add or remove a user from a friends list """
    users_profile = get_object_or_404(Profile, pk=user_id)
    if (request.user != users_profile.user):
        if request.user in users_profile.followers.all():
            users_profile.followers.remove(request.user)
            messages.success(request, f"You have unfollowed "
                             f"{users_profile.user}")
        else:
            users_profile.followers.add(request.user)
            messages.success(request, f"You have followed "
                             f"{users_profile.user}")
    else:
        messages.error(request, "You cannot follow your own profile!")

    return redirect('user_profile', profile_id=user_id)
