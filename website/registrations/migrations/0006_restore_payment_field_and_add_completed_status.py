# Generated by Django 2.0.1 on 2018-02-03 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0005_move_payment_model_to_app'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='payment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registrations_entry', to='payments.Payment'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='status',
            field=models.CharField(choices=[('confirm', 'Awaiting email confirmation'), ('review', 'Ready for review'), ('rejected', 'Rejected'), ('accepted', 'Accepted'), ('completed', 'Completed')], default='confirm', max_length=20, verbose_name='status'),
        ),
    ]