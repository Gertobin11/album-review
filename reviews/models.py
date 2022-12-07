from django.db import models
from django.contrib import auth
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


YEAR_CHOICES = []

for i in range(1900, (int(datetime.datetime.now().year) + 1)):
    YEAR_CHOICES.append((i, i))


class RecordCompany(models.Model):
    """ Company that publishes the albums """
    name = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


class Artist(models.Model):
    """ The artists who recorded the album """
    name = models.CharField(max_length=70)
    date_formed = models.DateField()
    website = models.URLField(verbose_name='The artists website')

    def __str__(self):
        return self.name


class Genre(models.Model):
    """ The Genre of the reviewed model """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Album(models.Model):
    """ The Album that will be reviewed """
    title = models.CharField(max_length=70)
    year_of_release = models.PositiveIntegerField(choices=YEAR_CHOICES,
                                                  verbose_name='The year the'
                                                  ' album was released')
    record_company = models.ForeignKey(RecordCompany, on_delete=models.CASCADE)
    album_cover = models.ImageField(upload_to='album_covers/',
                                    help_text='Upload Album Cover')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    """ The Users Album Review """
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                 MaxValueValidator(10)])
    date_created_on = models.DateTimeField(auto_now_add=True)
    date_edited_on = models.DateTimeField(blank=True, null=True)
    creator = models.ForeignKey(auth.get_user_model(),
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.album} reviewed by {self.creator}'
