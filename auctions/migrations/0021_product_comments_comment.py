# Generated by Django 3.2.dev20200804083438 on 2021-01-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_product_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_comments',
            name='comment',
            field=models.CharField(default='', max_length=400),
        ),
    ]