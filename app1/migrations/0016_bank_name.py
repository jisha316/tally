# Generated by Django 4.0.4 on 2022-08-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_delete_create_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
