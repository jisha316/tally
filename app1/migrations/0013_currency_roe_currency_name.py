# Generated by Django 4.0.4 on 2022-08-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_company_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency_roe',
            name='currency_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]