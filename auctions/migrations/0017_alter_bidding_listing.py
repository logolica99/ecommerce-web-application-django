# Generated by Django 3.2.dev20200804083438 on 2020-12-29 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_product_won'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidding', to='auctions.listing'),
        ),
    ]