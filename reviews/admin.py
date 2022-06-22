from django.contrib import admin
from reviews.models import Artist, Album, Genre, RecordCompany, Review


admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(RecordCompany)
admin.site.register(Review)
admin.site.register(Album)