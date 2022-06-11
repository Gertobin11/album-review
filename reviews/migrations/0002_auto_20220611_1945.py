# Generated by Django 3.2 on 2022-06-11 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the album', max_length=70)),
                ('year_of_release', models.DateField(verbose_name='The year the album was released')),
                ('album_cover', models.ImageField(help_text='The image from the album cover', upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the recording artist', max_length=70)),
                ('date_formed', models.DateField(verbose_name='The year the artists started')),
                ('website', models.URLField(verbose_name='The artists website')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the category', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='The review text')),
                ('rating', models.IntegerField(help_text='The rating the user has given the album')),
                ('date_created_on', models.DateTimeField(auto_now_add=True, help_text='The date and time the review was created')),
                ('date_edited_on', models.DateTimeField(help_text='The date the review was last edited', null=True)),
                ('album', models.ForeignKey(help_text='The album this review is for', on_delete=django.db.models.deletion.CASCADE, to='reviews.album')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='record_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.recordcompany'),
        ),
    ]