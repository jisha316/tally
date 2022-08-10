# Generated by Django 4.0.4 on 2022-08-10 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_remove_currency_roe_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency_roe',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tally_currency'),
        ),
        migrations.AlterField(
            model_name='currency_roe',
            name='currency_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
