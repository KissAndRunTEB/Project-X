# Generated by Django 4.2 on 2023-06-14 19:38

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_videospagegalleryimage'),
        ('snapshots', '0007_snapshotspage_tierhonorable_snapshotspage_tierthree_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='snapshotspage',
            name='videos',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, help_text='Select multiple Videos for this Snapshot', related_name='snapshots_videos', to='videos.videospage'),
        ),
    ]
