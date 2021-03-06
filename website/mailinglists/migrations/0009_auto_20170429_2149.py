# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 19:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglists', '0008_auto_20170412_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listalias',
            name='alias',
            field=models.CharField(help_text='Enter an alternative name for the list.', max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a simpler name', regex='^[a-zA-Z0-9]+$')], verbose_name='Alternative name'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='name',
            field=models.CharField(help_text='Enter the name for the list (i.e. name@thalia.nu).', max_length=100, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a simpler name', regex='^[a-zA-Z0-9]+$')], verbose_name='Name'),
        ),
    ]
