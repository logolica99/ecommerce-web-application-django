# Generated by Django 3.2.dev20200804083438 on 2021-01-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_product_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='active',
            field=models.CharField(choices=[('Active', 'Active'), ('Close', 'Close')], default='Active', max_length=200, null=True),
        ),
    ]
