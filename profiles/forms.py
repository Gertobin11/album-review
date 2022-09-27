from django import forms
from .models import Profile


class EditProfileForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = Profile
