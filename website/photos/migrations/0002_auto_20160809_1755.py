# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=photos.models.photo_uploadto)),
                ('rotation', models.IntegerField(default=0)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='_cover',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='covered_album', to='photos.Photo'),
        ),
    ]
