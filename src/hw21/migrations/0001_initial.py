# Generated by Django 2.2.1 on 2019-05-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicBand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('style', models.CharField(default=None, max_length=255)),
                ('birth_year', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
