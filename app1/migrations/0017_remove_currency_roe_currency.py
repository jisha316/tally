# Generated by Django 4.0.4 on 2022-08-10 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_currency_roe_currency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency_roe',
            name='currency',
        ),
    ]
