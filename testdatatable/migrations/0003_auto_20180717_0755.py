# Generated by Django 2.0.7 on 2018-07-17 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testdatatable', '0002_auto_20180717_0707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['name'], 'verbose_name': 'Artist', 'verbose_name_plural': 'Artists'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name'], 'verbose_name': 'Genre', 'verbose_name_plural': 'Genres'},
        ),
    ]
