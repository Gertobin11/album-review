from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from reviews.models import Genre


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    friends = models.ManyToManyField(User, related_name='friends')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    favourite_genre = models.ForeignKey(Genre, on_delete=models.CASCADE,
                                        blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.user}'s Profile"


def create_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, sender=User)
