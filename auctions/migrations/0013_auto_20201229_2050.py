# Generated by Django 3.2.dev20200804083438 on 2020-12-29 14:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20201229_2046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bidding',
            old_name='Listing',
            new_name='listing',
        ),
        migrations.AddField(
            model_name='bidding',
            name='bidded_user',
            field=models.ManyToManyField(blank=True, related_name='bidding', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='bidding',
            name='bid',
        ),
        migrations.AddField(
            model_name='bidding',
            name='bid',
            field=models.IntegerField(default=0),
        ),
    ]