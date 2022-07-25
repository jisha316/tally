# Generated by Django 4.0.4 on 2022-07-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cost_centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre_name', models.CharField(max_length=255)),
                ('centre_alias', models.CharField(max_length=255)),
                ('centre_under', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='tally_currency',
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
        migrations.CreateModel(
            name='tally_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=255)),
                ('group_alias', models.CharField(max_length=255)),
                ('group_under', models.CharField(max_length=255)),
                ('nature', models.CharField(max_length=255, null=True)),
                ('gross_profit', models.CharField(max_length=255, null=True)),
                ('sub_ledger', models.CharField(max_length=255)),
                ('debit_credit', models.CharField(max_length=255)),
                ('calculation', models.CharField(max_length=255)),
                ('invoice', models.CharField(max_length=255)),
            ],
        ),
    ]
