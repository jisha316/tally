# Generated by Django 4.0.4 on 2022-07-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_gst_lutbond_gst_taxability_delete_vouchers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gst_taxability',
            name='applicable_dt',
            field=models.DateField(null=True),
        ),
    ]