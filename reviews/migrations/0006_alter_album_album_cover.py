# Generated by Django 3.2 on 2022-06-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_album_year_of_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_cover',
            field=models.ImageField(help_text='The image from the album cover', upload_to='album_covers/'),
        ),
    ]