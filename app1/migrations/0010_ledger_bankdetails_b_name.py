# Generated by Django 4.0.4 on 2022-08-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_company_features_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger_bankdetails',
            name='b_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
