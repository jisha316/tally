# Generated by Django 4.0.4 on 2022-07-30 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_currency_roe'),
    ]

    operations = [
        migrations.CreateModel(
            name='gst_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=255)),
                ('registration_type', models.CharField(max_length=50)),
                ('assessee_territory', models.CharField(max_length=50)),
                ('gst_applicable', models.DateField(null=True)),
                ('gstin_uin', models.CharField(max_length=100)),
                ('periodicity', models.CharField(max_length=50)),
                ('kerala_fca', models.CharField(max_length=20, null=True)),
                ('applicable_from', models.DateField(null=True)),
                ('gst_rate_details', models.CharField(max_length=20)),
                ('tl_advanceR', models.CharField(max_length=20)),
                ('tl_reverseC', models.CharField(max_length=20)),
                ('gst_classification', models.CharField(max_length=20)),
                ('lut_bond', models.CharField(max_length=20)),
                ('tax_rate', models.CharField(max_length=20)),
                ('tax_calculation', models.CharField(max_length=100)),
                ('tax_purchase', models.CharField(max_length=20)),
                ('e_waybillA', models.CharField(max_length=20)),
                ('applicable_f', models.DateField(null=True)),
                ('thresholdlimit_include', models.CharField(max_length=255)),
                ('threshold_limit', models.IntegerField()),
                ('intrastate', models.CharField(max_length=20)),
                ('ithreshold_limit', models.IntegerField()),
                ('print_eway', models.CharField(max_length=20)),
                ('e_invoiceA', models.CharField(max_length=20)),
                ('app_from', models.DateField(null=True)),
                ('billfrom_place', models.CharField(max_length=50)),
                ('period_einvoiceR', models.CharField(max_length=50)),
                ('send_eW_details_einvoice', models.CharField(max_length=50)),
            ],
        ),
    ]