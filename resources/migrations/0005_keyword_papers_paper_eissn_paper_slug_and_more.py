# Generated by Django 5.1 on 2024-08-30 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_rename_result_keyword_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='papers',
            field=models.ManyToManyField(to='resources.paper'),
        ),
        migrations.AddField(
            model_name='paper',
            name='eISSN',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='paper',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 30, 14, 6, 0, 767051)),
        ),
    ]
