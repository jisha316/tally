# Generated by Django 4.0.4 on 2022-08-19 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_create_companies_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger_bankdetails',
            name='b_name',
        ),
    ]
