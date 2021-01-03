# Generated by Django 3.2.dev20200804083438 on 2021-01-03 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_alter_product_won_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auctions.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]