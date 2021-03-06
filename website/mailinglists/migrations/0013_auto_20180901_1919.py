# Generated by Django 2.0.8 on 2018-09-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activemembers', '0034_clean_up_models'),
        ('mailinglists', '0012_auto_20180203_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailinglist',
            name='committees',
        ),
        migrations.AddField(
            model_name='mailinglist',
            name='member_groups',
            field=models.ManyToManyField(blank=True, help_text='Select entire groups to include in the list.', to='activemembers.MemberGroup', verbose_name='Member groups'),
        ),
    ]
