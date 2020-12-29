# Generated by Django 3.2.dev20200804083438 on 2020-12-29 14:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_listing_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidding',
            name='bid',
        ),
        migrations.AddField(
            model_name='bidding',
            name='bid',
            field=models.ManyToManyField(blank=True, related_name='bidding', to=settings.AUTH_USER_MODEL),
        ),
    ]