# Generated by Django 4.2 on 2023-06-13 20:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamespage',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Post date'),
        ),
    ]
