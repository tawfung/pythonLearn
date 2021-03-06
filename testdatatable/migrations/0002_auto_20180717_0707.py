# Generated by Django 2.0.7 on 2018-07-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdatatable', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['name'], 'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['name'], 'verbose_name': ('Artist',), 'verbose_name_plural': 'Artists'},
        ),
        migrations.AddField(
            model_name='album',
            name='genres',
            field=models.ManyToManyField(related_name='albums', to='testdatatable.Genre', verbose_name='Genres'),
        ),
    ]
