# Generated by Django 3.0.8 on 2020-09-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0008_migrate_processing_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='processing_date',
        ),
        migrations.AlterField(
            model_name='payment',
            name='type',
            field=models.CharField(choices=[('cash_payment', 'Cash payment'), ('card_payment', 'Card payment'), ('tpay_payment', 'Thalia Pay payment'), ('wire_payment', 'Wire payment')], max_length=20, verbose_name='type'),
        ),
    ]