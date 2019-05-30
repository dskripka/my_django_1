# Generated by Django 2.2.1 on 2019-05-28 13:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default=None, max_length=30)),
                ('model', models.CharField(default=None, max_length=20)),
                ('color', models.CharField(default=None, max_length=20)),
                ('weight', models.PositiveSmallIntegerField()),
                ('owner_full_name', models.CharField(default=None, max_length=50)),
                ('year_issue', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1900)])),
            ],
        ),
    ]