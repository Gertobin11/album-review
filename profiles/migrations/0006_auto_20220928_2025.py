# Generated by Django 3.2 on 2022-09-28 20:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0005_rename_friends_profile_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follow',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
    ]