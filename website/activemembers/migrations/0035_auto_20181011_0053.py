# Generated by Django 2.0.8 on 2018-10-10 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activemembers', '0034_clean_up_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membergroup',
            name='name_en',
            field=models.CharField(max_length=40, unique=True, verbose_name='Name (EN)'),
        ),
        migrations.AlterField(
            model_name='membergroup',
            name='name_nl',
            field=models.CharField(max_length=40, unique=True, verbose_name='Name (NL)'),
        ),
        migrations.AlterField(
            model_name='membergroupmembership',
            name='chair',
            field=models.BooleanField(default=False, help_text='There can only be one chair at a time!', verbose_name='Chair of the group'),
        ),
        migrations.AlterField(
            model_name='membergroupmembership',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activemembers.MemberGroup', verbose_name='Group'),
        ),
    ]
