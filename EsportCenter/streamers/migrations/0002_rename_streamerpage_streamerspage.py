# Generated by Django 4.2 on 2023-06-10 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('streamers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StreamerPage',
            new_name='StreamersPage',
        ),
    ]
