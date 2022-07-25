
from django.db import models

# Create your models here.


class tally_group(models.Model):
    group_name = models.CharField(max_length=255)
    group_alias = models.CharField(max_length=255)
    group_under = models.CharField(max_length=255)
    nature = models.CharField(max_length=255,null=True)
    gross_profit = models.CharField(max_length=255 ,null=True)
    sub_ledger = models.CharField(max_length=255)
    debit_credit = models.CharField(max_length=255)
    calculation = models.CharField(max_length=255)
    invoice = models.CharField(max_length=255)

class tally_currency(models.Model):
    c_symbol = models.CharField(max_length=255)
    formal_name = models.CharField(max_length=255)
    iso_Ccode = models.CharField(max_length=30,null=True)
    decimal_place = models.IntegerField()
    show_amtM = models.CharField(max_length=20)
    suffix_smblA = models.CharField(max_length=20)
    add_space = models.CharField(max_length=20)
    word_rep = models.CharField(max_length=255,null=True)
    no_decimal = models.IntegerField()

class alt_currency(models.Model):
    c_symbol = models.CharField(max_length=255)
    formal_name = models.CharField(max_length=255)
    iso_Ccode = models.CharField(max_length=30,null=True)
    decimal_place = models.IntegerField()
    show_amtM = models.CharField(max_length=20)
    suffix_smblA = models.CharField(max_length=20)
    add_space = models.CharField(max_length=20)
    word_rep = models.CharField(max_length=255,null=True)
    no_decimal = models.IntegerField()

class cost_centre(models.Model):
    centre_name=models.CharField(max_length=255)
    centre_alias = models.CharField(max_length=255)
    centre_under = models.CharField(max_length=255)
