from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('search-results', views.search_results, name='search'),
    path('review-list/', views.review_list, name='review_list'),
    path('album-list/', views.album_list, name='album_list'),
    path('album-view/<int:id>', views.album_view, name='album_view'),
    path('review/<int:id>', views.review, name='review')
    ]
