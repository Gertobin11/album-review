from django import forms

CHOICES = (('album', 'album'), ('reviewer', 'reviewer'), ('group', 'group'))


class SearchForm(forms.Form):
    search = forms.CharField(max_length=70, min_length=3, required=False)
    search_in = forms.ChoiceField(choices=CHOICES, required=False)

    search.widget.attrs.update({'placeholder': 'Enter Search term'})
