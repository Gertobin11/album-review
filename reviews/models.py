from django.db import models
from django.contrib import auth


class RecordCompany(models.Model):
    """ Company that publishes the albums """
    name = models.CharField(max_length=50, help_text='The name of the record company')
    website = models.URLField(help_text='The Companies website')

    def __str__(self):
        return self.name


class Artist(models.Model):
    """ The artists who recorded the album """
    name = models.CharField(max_length=70, help_text='The name of the recording artist')
    date_formed = models.DateField('The year the artists started')
    website = models.URLField(verbose_name='The artists website')

    def __str__(self):
        return self.name


class Genre(models.Model):
    """ The Genre of the reviewed model """
    name = models.CharField(max_length=50, help_text='The name of the category')

    def __str__(self):
        return self.name


class Album(models.Model):
    """ The Album that will be reviewed """
    title = models.CharField(max_length=70, help_text='The title of the album')
    year_of_release = models.DateField(verbose_name='The year the album was released')
    record_company = models.ForeignKey(RecordCompany, on_delete=models.CASCADE)
    album_cover = models.ImageField(upload_to='media/', help_text='The image from the album cover')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    """ The Users Album Review """
    content = models.TextField(help_text='The review text')
    rating = models.IntegerField(help_text='The rating the user has given the album')
    date_created_on = models.DateTimeField(auto_now_add=True, help_text='The date and time the review was created')
    date_edited_on = models.DateTimeField(null=True, help_text='The date the review was last edited')
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, help_text='The album this review is for')

    def __str__(self):
        return f'{self.album} reviewed by {self.creator}'
