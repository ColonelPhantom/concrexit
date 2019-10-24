# Generated by Django 2.2.1 on 2019-10-13 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglists', '0014_mailinglist_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listalias',
            options={'verbose_name': 'List alias', 'verbose_name_plural': 'List aliases'},
        ),
        migrations.RemoveField(
            model_name='mailinglist',
            name='autoresponse_enabled',
        ),
        migrations.RemoveField(
            model_name='mailinglist',
            name='autoresponse_text',
        ),
        migrations.RemoveField(
            model_name='mailinglist',
            name='prefix',
        ),
        migrations.RemoveField(
            model_name='mailinglist',
            name='archived',
        ),
        migrations.AlterField(
            model_name='listalias',
            name='mailinglist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='mailinglists.MailingList', verbose_name='Mailing list'),
        ),
    ]
