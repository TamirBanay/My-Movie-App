# Generated by Django 4.2.5 on 2023-10-16 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_favoritegoogleusers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavoriteGoogleUsers',
            new_name='Favorite_Google_Users',
        ),
    ]
