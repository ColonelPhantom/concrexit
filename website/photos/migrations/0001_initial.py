# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-03 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('dirname', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
    ]
