from django import forms

from .models import Album, Artist, Review, RecordCompany, Genre

CHOICES = (('album', 'album'), ('reviewer', 'reviewer'), ('group', 'group'))


class SearchForm(forms.Form):
    search = forms.CharField(max_length=70, min_length=3, required=False)
    search_in = forms.ChoiceField(choices=CHOICES, required=False)

    search.widget.attrs.update({'placeholder': 'Enter Search term'})


class ArtistForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Artist
        widgets = {'name': forms.TextInput(
                   attrs={'placeholder': 'Enter Artists name'}),
                   'date_formed': forms.TextInput(
                   attrs={'placeholder': ('Artists '
                                          'Year of formation yyyy-mm-dd')}),
                   'website': forms.TextInput(
                    attrs={'placeholder': 'Enter Artists Website'})
                   }


class GenreForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Genre
        widgets = {'name': forms.TextInput(
                   attrs={'placeholder': 'Enter Genre Name'})}


class RecordCompanyForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = RecordCompany
        widgets = {'name': forms.TextInput(
                   attrs={'placeholder': 'Enter Record Label Name'}),
                   'website': forms.TextInput(
                    attrs={'placeholder': 'Enter Record Labels Website'})}


class AlbumForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Album
        widgets = {'title': forms.TextInput(
                   attrs={'placeholder': 'Enter Title Of The Album'})}
