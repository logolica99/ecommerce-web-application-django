# Generated by Django 3.2.dev20200804083438 on 2020-12-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Home', 'Home'), ('Health', 'Health'), ('Sports', 'Sports')], max_length=200, null=True),
        ),
    ]