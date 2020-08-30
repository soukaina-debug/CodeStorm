# Generated by Django 3.0.4 on 2020-05-20 18:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_doubt_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doubt',
            name='like_doubt',
            field=models.ManyToManyField(blank=True, related_name='likes_doubt', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reply',
            name='like_reply',
            field=models.ManyToManyField(blank=True, related_name='likes_reply', to=settings.AUTH_USER_MODEL),
        ),
    ]