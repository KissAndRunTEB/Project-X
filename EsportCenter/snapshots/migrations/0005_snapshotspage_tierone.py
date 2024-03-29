# Generated by Django 4.2 on 2023-06-14 18:47

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0002_alter_deckspage_date'),
        ('snapshots', '0004_snapshotspage_authors_snapshotspage_patreons_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='snapshotspage',
            name='tierone',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, help_text='Select multiple Decks for this Snapshot', null=True, related_name='snapshots', to='decks.deckspage'),
        ),
    ]
