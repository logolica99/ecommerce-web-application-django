# Generated by Django 3.2.dev20200804083438 on 2020-12-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20201229_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='active',
            field=models.CharField(choices=[('Active', 'Active'), ('Close', 'Close')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Home', 'Home'), ('Health', 'Health'), ('Sports', 'Sports')], max_length=200, null=True),
        ),
    ]
