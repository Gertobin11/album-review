from django.contrib import admin
from reviews.models import Artist, Album, Genre, RecordCompany, Review


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'year_of_release')
    search_fields = ['title', 'artist__name']
    ordering = ['title']
    list_filter = ['genre__name']
    

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_formed')
    search_fields = ['name']
    ordering = ['name']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']


@admin.register(RecordCompany)
class RecordCompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'album', 'date_created_on')
    search_fields = ['title', 'creator__username', 'album__title']
    ordering = ['-date_created_on']