# Generated by Django 5.1 on 2024-08-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_paper_outside_searchresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('result', models.ManyToManyField(to='resources.searchresult')),
            ],
        ),
    ]
