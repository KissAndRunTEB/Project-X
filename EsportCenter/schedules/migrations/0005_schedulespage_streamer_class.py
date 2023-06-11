# Generated by Django 4.2 on 2023-06-10 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('streamers', '0003_rename_country_streamerspage_language'),
        ('schedules', '0004_alter_schedulespage_hourfriday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulespage',
            name='streamer_class',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_page', to='streamers.streamerspage'),
        ),
    ]
