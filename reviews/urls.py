from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('search_results', views.search_results, name='search'),
    path('review-list/', views.review_list, name='review_list')
    ]