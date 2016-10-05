# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_member_initials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='display_name_preference',
            field=models.CharField(choices=[('full', 'Show full name'), ('nickname', 'Show only nickname'), ('firstname', 'Show only first name'), ('initials', 'Show initials and last name'), ('fullnick', 'Show name like "John \'nickname\' Doe"'), ('nicklast', 'Show nickname and last name')], default='full', max_length=10, verbose_name='How to display name'),
        ),
    ]
