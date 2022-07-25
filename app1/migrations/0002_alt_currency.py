# Generated by Django 4.0.4 on 2022-07-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='alt_currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_symbol', models.CharField(max_length=255)),
                ('formal_name', models.CharField(max_length=255)),
                ('iso_Ccode', models.CharField(max_length=30, null=True)),
                ('decimal_place', models.IntegerField()),
                ('show_amtM', models.CharField(max_length=20)),
                ('suffix_smblA', models.CharField(max_length=20)),
                ('add_space', models.CharField(max_length=20)),
                ('word_rep', models.CharField(max_length=255, null=True)),
                ('no_decimal', models.IntegerField()),
            ],
        ),
    ]