from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('review-list/', views.review_list, name='review_list'),
    path('album-list/', views.album_list, name='album_list'),
    path('album-view/<int:id>/', views.album_view, name='album_view'),
    path('review/<int:id>/', views.review, name='review'),
    path('search-results/', views.search, name='search'),
    path('advanced-search/', views.advanced_sarch, name='advanced_search'),
    path('add-review/', views.add_review, name='add_review'),
    path('add-artist', views.add_artist, name='add_artist')
    ]
