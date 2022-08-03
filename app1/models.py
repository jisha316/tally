
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

class tally_vouchers(models.Model):
    voucher_name = models.CharField(max_length=255,null=True)
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

class currency_ROE(models.Model):
    date_ROE = models.DateField()
    currency = models.ForeignKey(tally_currency,on_delete = models.CASCADE,null = True)
    std_rate = models.CharField(max_length=20,null=True)
    selling_SR = models.CharField(max_length=20,null=True)
    buying_SR = models.CharField(max_length=20,null=True)
    
class tally_gst(models.Model):
    state = models.CharField(max_length=255,null=True)
    registration_type = models.CharField(max_length=50,null=True)
    assessee_territory = models.CharField(max_length=50,null=True)
    gst_applicable = models.DateField(null=True)
    gstin_uin = models.CharField(max_length=100,null=True)
    periodicity = models.CharField(max_length=50,null=True)
    kerala_fca = models.CharField(max_length=20,null=True)
    applicable_from = models.DateField(null=True)
    gst_rate_details = models.CharField(max_length=20,null=True)
    tl_advanceR = models.CharField(max_length=20,null=True)
    tl_reverseC = models.CharField(max_length=20,null=True)
    gst_classification = models.CharField(max_length=20,null=True)
    lut_bond = models.CharField(max_length=20,null=True)
    tax_rate = models.CharField(max_length=20,null=True)
    tax_calculation = models.CharField(max_length=100,null=True)
    tax_purchase = models.CharField(max_length=20,null=True)
    
    e_waybillA = models.CharField(max_length=20,null=True)
    applicable_f = models.DateField(null=True)
    thresholdlimit_include = models.CharField(max_length=255,null=True)
    threshold_limit = models.IntegerField(null=True)
    intrastate = models.CharField(max_length=20,null=True)
    ithreshold_limit = models.IntegerField(null=True)
    print_eway = models.CharField(max_length=20,null=True)

    e_invoiceA = models.CharField(max_length=20,null=True)
    app_from = models.DateField(null=True)
    billfrom_place = models.CharField(max_length=50,null=True)
    period_einvoiceR = models.CharField(max_length=50,null=True)
    send_eW_details_einvoice = models.CharField(max_length=50,null=True)

class gst_lutbond(models.Model):
    # gst = models.ForeignKey(tally_gst,on_delete = models.CASCADE,null = True)
    lut_bond_No = models.CharField(max_length=50)
    validity_from = models.DateField()
    validity_to = models.DateField()

class gst_taxability(models.Model):
    # gst2 = models.ForeignKey(tally_gst,on_delete = models.CASCADE,null = True)
    taxability = models.CharField(max_length=50)
    applicable_dt = models.DateField(null=True)
    integrated_tax = models.CharField(max_length=50)
    cess = models.CharField(max_length=50)
    flood_cess = models.CharField(max_length=50)

class tally_ledger(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    under = models.CharField(max_length=255)
    grp = models.ForeignKey(tally_group,on_delete = models.CASCADE,null = True)
    mname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.IntegerField()
    bank_details = models.CharField(max_length=20,null=True)
    pan_no = models.CharField(max_length=100)
    registration_type = models.CharField(max_length=100)
    gst_uin = models.CharField(max_length=100)
    opening_blnc = models.IntegerField()

    set_odl = models.CharField(max_length=255,null=True)
    ac_holder_nm = models.CharField(max_length=255,null=True)
    acc_no = models.CharField(max_length=255,null=True)
    ifsc_code = models.CharField(max_length=255,null=True)
    swift_code = models.CharField(max_length=255,null=True)
    bank_name = models.CharField(max_length=255,null=True)
    branch = models.CharField(max_length=255,null=True)
    SA_cheque_bk = models.CharField(max_length=20,null=True)
    Echeque_p = models.CharField(max_length=20,null=True)
    SA_chequeP_con = models.CharField(max_length=20,null=True)

    
    
    



