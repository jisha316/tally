# Generated by Django 4.0.4 on 2022-08-03 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_ledger_bankac_acc_nm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ledger_bankac',
            old_name='acc_nm',
            new_name='acc_no',
        ),
    ]