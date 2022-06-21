# Generated by Django 3.2 on 2022-06-21 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_alter_album_album_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='album',
            field=models.ForeignKey(help_text='The album this review is for', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.album'),
        ),
    ]
