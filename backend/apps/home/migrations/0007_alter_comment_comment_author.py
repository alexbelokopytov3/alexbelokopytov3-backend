# Generated by Django 4.0.6 on 2022-08-11 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_comment_active_alter_comment_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]