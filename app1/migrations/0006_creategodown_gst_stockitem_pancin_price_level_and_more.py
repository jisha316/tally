# Generated by Django 4.0.4 on 2022-08-29 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_currencyalteration_rateofexchange_voucher_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateGodown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('under_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='gst_stockitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calc_typ', models.CharField(max_length=100)),
                ('taxability', models.CharField(max_length=100)),
                ('tax', models.CharField(max_length=100)),
                ('cess', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pancin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan', models.CharField(max_length=30)),
                ('cin', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Price_level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='revised_applicability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appl_from', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='revised_applicability_composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appl_from_c', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='stockcatagorycreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('under', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='stockgroupcreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alias', models.CharField(max_length=100)),
                ('under', models.CharField(max_length=100)),
                ('quantities', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='unit_simple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=100)),
                ('formal_name', models.CharField(max_length=100)),
                ('uqc', models.CharField(max_length=100)),
                ('decimal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='unit_compound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=100)),
                ('conversion', models.IntegerField()),
                ('s_unit', models.IntegerField(null=True)),
                ('unit_simple', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.unit_simple')),
            ],
        ),
        migrations.CreateModel(
            name='stock_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100, null=True)),
                ('alias', models.CharField(max_length=100, null=True)),
                ('gst_applicable', models.CharField(max_length=100)),
                ('typ_sply', models.CharField(max_length=100)),
                ('set_alter', models.CharField(max_length=100)),
                ('rate_of_duty', models.IntegerField()),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('per', models.CharField(max_length=100, null=True)),
                ('value', models.CharField(max_length=100, null=True)),
                ('stockgroupcreation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.stockgroupcreation')),
                ('unit_compound', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.unit_compound')),
            ],
        ),
    ]
