# Generated by Django 5.1 on 2024-08-28 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_keyword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='keyword',
            old_name='result',
            new_name='results',
        ),
    ]
