# Generated by Django 4.0.4 on 2022-08-17 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_person_res_details_area_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_company',
            name='fax',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='create_company',
            name='mobile_no',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='create_company',
            name='pincode',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='create_company',
            name='telephone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='create_company',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
