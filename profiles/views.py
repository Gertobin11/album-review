from django.shortcuts import render
from .models import Profile


def profiles(request):
    """ Return all created profiles"""
    profiles = Profile.objects.all()
    template = 'profiles.html'
    context = {
        'profles': profiles
    }
    return render(request, template, context)
