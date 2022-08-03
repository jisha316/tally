# Generated by Django 4.0.4 on 2022-08-03 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_gst_lutbond_gst_taxability'),
    ]

    operations = [
        migrations.CreateModel(
            name='tally_ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('under', models.CharField(max_length=255)),
                ('mname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('pincode', models.IntegerField()),
                ('bank_details', models.CharField(max_length=20, null=True)),
                ('pan_no', models.CharField(max_length=100)),
                ('registration_type', models.CharField(max_length=100)),
                ('gst_uin', models.CharField(max_length=100)),
                ('SA_gst', models.CharField(max_length=20)),
                ('grp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tally_group')),
            ],
        ),
        migrations.CreateModel(
            name='ledger_bankac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_odl', models.CharField(max_length=255, null=True)),
                ('ac_holder_nm', models.CharField(max_length=255, null=True)),
                ('ifsc_code', models.CharField(max_length=255, null=True)),
                ('swift_code', models.CharField(max_length=255, null=True)),
                ('bank_name', models.CharField(max_length=255, null=True)),
                ('branch', models.CharField(max_length=255, null=True)),
                ('SA_cheque_bk', models.CharField(max_length=20, null=True)),
                ('Echeque_p', models.CharField(max_length=20, null=True)),
                ('SA_chequeP_con', models.CharField(max_length=20, null=True)),
                ('ledger', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tally_ledger')),
            ],
        ),
    ]
