# Generated by Django 5.1 on 2024-08-30 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_comment_created_at_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 30, 14, 27, 50, 21049)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 30, 14, 27, 50, 21049)),
        ),
    ]
