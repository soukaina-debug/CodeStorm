# Generated by Django 3.0.4 on 2020-05-20 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_doubt_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='author',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='doubt_id',
        ),
        migrations.DeleteModel(
            name='Doubt',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
