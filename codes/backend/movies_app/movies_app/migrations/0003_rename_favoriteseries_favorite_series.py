# Generated by Django 4.2.5 on 2023-10-28 13:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies_app', '0002_favoriteseries'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavoriteSeries',
            new_name='Favorite_series',
        ),
    ]
