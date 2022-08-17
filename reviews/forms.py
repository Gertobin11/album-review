from django import forms

CHOICES = (('album', 'album'), ('reviwer', 'reviwer'), ('group', 'group'))


class SearchForm(forms.Form):
    search = forms.CharField(max_length=70, min_length=3, required=False)
    title = forms.ChoiceField(choices=CHOICES, required=False)
