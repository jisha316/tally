
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

class tally_tds(models.Model):
    tan_reg_no = models.CharField(max_length=40)
    tax_ded_clctn = models.CharField(max_length=40)
    deductor_type = models.CharField(max_length=100)
    ded_brachdevision = models.CharField(max_length=255)
    person_res = models.CharField(max_length=255)
    ignore_it = models.CharField(max_length=40)
    tds_stock_items = models.CharField(max_length=40)

class person_res_details(models.Model):
    tds = models.ForeignKey(tally_tds,on_delete = models.CASCADE,null = True)
    name = models.CharField(max_length=255,null=True)
    son_daughter = models.CharField(max_length=255,null=True)
    designation = models.CharField(max_length=255,null=True)
    pan = models.CharField(max_length=255,null=True)
    flat_no = models.CharField(max_length=10,null=True)
    premise_name = models.CharField(max_length=255,null=True)
    street = models.CharField(max_length=255,null=True)
    area = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    pincode = models.IntegerField(null=True)
    mobile_no = models.IntegerField(null=True)
    std_code = models.IntegerField(null=True)
    telephone = models.IntegerField(null=True)
    email = models.EmailField(null=True)

class vouchers(models.Model):
    name = models.CharField(max_length=255,null=True)
    alias = models.CharField(max_length=255,null=True)
    voucher_type = models.CharField(max_length=255,null=True)
    Abbreviation = models.CharField(max_length=255,null=True)
    activate_Vtype = models.CharField(max_length=20,null=True)
    method_Vno = models.CharField(max_length=200,null=True)
    prevent = models.CharField(max_length=20,null=True)
    advance_con = models.CharField(max_length=20,null=True)
    use_EDV = models.CharField(max_length=20,null=True)
    zero_val = models.CharField(max_length=20,null=True)
    mVoptional_defualt = models.CharField(max_length=20,null=True)
    allow_nar = models.CharField(max_length=20,null=True)
    provide_L = models.CharField(max_length=20,null=True)
    manu_jrnl = models.CharField(max_length=20,null=True)
    track_purchase = models.CharField(max_length=20,null=True)
    enable_acc = models.CharField(max_length=20,null=True)
    prnt_VA_save = models.CharField(max_length=20,null=True)
    prnt_frml = models.CharField(max_length=20,null=True)
    jurisdiction = models.CharField(max_length=20,null=True)
    title_print = models.CharField(max_length=20,null=True)
    set_alter = models.CharField(max_length=20,null=True)
    pos_invoice = models.CharField(max_length=20,null=True)
    msg_1 = models.CharField(max_length=255,null=True)
    msg_2 = models.CharField(max_length=255,null=True)
    default_bank = models.CharField(max_length=255,null=True)
    name_class = models.CharField(max_length=255,null=True)
