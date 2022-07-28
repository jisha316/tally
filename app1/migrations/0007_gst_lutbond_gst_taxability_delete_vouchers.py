# Generated by Django 4.0.4 on 2022-07-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_tally_vouchers'),
    ]

    operations = [
        migrations.CreateModel(
            name='gst_lutbond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lut_bond_No', models.CharField(max_length=50)),
                ('validity_from', models.DateField()),
                ('validity_to', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='gst_taxability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxability', models.CharField(max_length=50)),
                ('applicable_dt', models.DateField()),
                ('integrated_tax', models.CharField(max_length=50)),
                ('cess', models.CharField(max_length=50)),
                ('flood_cess', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='vouchers',
        ),
    ]
