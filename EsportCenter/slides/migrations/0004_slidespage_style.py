# Generated by Django 4.2 on 2023-06-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0003_slidesindexpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidespage',
            name='style',
            field=models.CharField(choices=[('option1', 'News left'), ('option2', 'News central'), ('option3', 'Special')], default='option1', max_length=20),
        ),
    ]
