from django.shortcuts import render
from .models import Profile


def profiles(request):
    """ Return all created profiles"""
    profiles = Profile.objects.all()
    template = 'profiles.html'
    print(profiles)
    context = {
        'profiles': profiles
    }
    return render(request, template, context)
