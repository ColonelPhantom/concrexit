# Generated by Django 3.0.2 on 2020-02-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_auto_20191030_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='topic',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]