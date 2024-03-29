# Generated by Django 4.2 on 2023-06-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamers', '0003_rename_country_streamerspage_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamerspage',
            name='InstagramLink',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='streamerspage',
            name='TiktokLink',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='streamerspage',
            name='TwitchLink',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='streamerspage',
            name='TwitterLink',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='streamerspage',
            name='YoutubeLink',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
