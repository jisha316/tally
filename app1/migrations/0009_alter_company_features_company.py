# Generated by Django 4.0.4 on 2022-08-19 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_create_companies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_features',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.create_companies'),
        ),
    ]
