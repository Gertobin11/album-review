from django import forms
from .models import Profile


class EditProfileForm(forms.ModelForm):
    class Meta:
        fields = ['first_name', 'last_name', 'favourite_genre', 'profile_pic']
        model = Profile
