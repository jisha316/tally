# Generated by Django 4.0.4 on 2022-09-02 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_remove_stock_item_stockgroupcreation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock_item',
            old_name='name1',
            new_name='name',
        ),
    ]
