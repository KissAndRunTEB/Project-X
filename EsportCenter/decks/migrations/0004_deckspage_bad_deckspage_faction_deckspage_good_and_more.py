# Generated by Django 4.2 on 2023-06-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0003_deckspage_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='deckspage',
            name='bad',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='deckspage',
            name='faction',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='deckspage',
            name='good',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='deckspage',
            name='link',
            field=models.CharField(default='', max_length=250),
        ),
    ]
