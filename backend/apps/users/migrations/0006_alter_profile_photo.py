# Generated by Django 4.0.6 on 2022-08-04 08:27

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to=users.models.url_directory),
        ),
    ]