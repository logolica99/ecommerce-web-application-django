# Generated by Django 3.2.dev20200804083438 on 2020-12-29 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_listing_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='bidding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField()),
                ('Listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidding', to='auctions.listing', unique=True)),
            ],
        ),
    ]
