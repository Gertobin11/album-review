# Generated by Django 3.2 on 2022-09-28 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20220928_0810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='friends',
            new_name='follow',
        ),
    ]