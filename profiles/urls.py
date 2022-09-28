from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profile_list'),
    path('<int:profile_id>', views.user_profile, name='user_profile'),
    path('follow/<int:user_id>', views.followers, name='follow')
]
