# Generated by Django 4.0.4 on 2022-08-12 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_delete_ledger_gst'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger_cheque_demension',
            name='ledger_name',
        ),
    ]
