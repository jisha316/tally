from django.db import models

# Create your models here.
class create_companies(models.Model):
    company_name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile_no = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20)
    formal_name = models.CharField(max_length=20)
    fin_begin = models.DateField()
    books_begin = models.DateField()
    fin_end = models.DateField()
    status=models.BooleanField(default=False)

class create_company(models.Model):
    company_name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile_no = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20)
    formal_name = models.CharField(max_length=20)
    fin_begin = models.DateField()
    books_begin = models.DateField()
    fin_end = models.DateField()
    status=models.BooleanField(default=False)

class company_features(models.Model):
    maintain_account = models.CharField(max_length=10)
    billwise_entry = models.CharField(max_length=10)
    cost_centre = models.CharField(max_length=10)
    interest_calculation = models.CharField(max_length=10)
    maintain_inventry = models.CharField(max_length=10)
    account_inventry = models.CharField(max_length=10)
    multiple_pricelevel = models.CharField(max_length=10)
    enable_batches = models.CharField(max_length=10)
    expiry_date = models.CharField(max_length=10)
    job_order_procress = models.CharField(max_length=10)
    cost_tracking = models.CharField(max_length=10)
    job_costing= models.CharField(max_length=10)
    discount_column = models.CharField(max_length=10)
    seperte_actual = models.CharField(max_length=10)
    gst = models.CharField(max_length=10)
    tds = models.CharField(max_length=10)
    tcs = models.CharField(max_length=10)
    vat = models.CharField(max_length=10)
    excise = models.CharField(max_length=10)
    service_tax = models.CharField(max_length=10)
    payroll = models.CharField(max_length=10)
    multiple_address = models.CharField(max_length=10)
    mark_modified = models.CharField(max_length=10)
    company=models.ForeignKey(create_companies,on_delete = models.CASCADE,null = True)

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
    lut_bond_No = models.CharField(max_length=50)
    validity_from = models.DateField()
    validity_to = models.DateField()
    

class gst_taxability(models.Model):
    taxability = models.CharField(max_length=50)
    applicable_dt = models.DateField(null=True)
    integrated_tax = models.CharField(max_length=50)
    cess = models.CharField(max_length=50)
    flood_cess = models.CharField(max_length=50)
    

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
    street = models.CharField(max_length=100,null=True)
    area = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=255,null=True)
    pincode = models.CharField(max_length=10,null=True)
    mobile_no = models.CharField(max_length=15,null=True)
    std_code = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=10,null=True)
    email = models.EmailField(null=True)
    

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

class crt_currency(models.Model):
    c_symbol = models.CharField(max_length=255)
    formal_name = models.CharField(max_length=255)
    iso_Ccode = models.CharField(max_length=30,null=True)
    decimal_place = models.IntegerField()
    show_amtM = models.CharField(max_length=20)
    suffix_smblA = models.CharField(max_length=20)
    add_space = models.CharField(max_length=20)
    word_rep = models.CharField(max_length=255,null=True)
    no_decimal = models.IntegerField()

class currency_ROE(models.Model):
    date_ROE = models.DateField()
    currency_name =models.CharField(max_length=20,null=True)
    std_rate = models.IntegerField(null=True)
    selling_SR = models.IntegerField(null=True)
    buying_SR = models.IntegerField(null=True)

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
    


class tally_ledger(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255,null=True)
    under = models.CharField(max_length=255)
    grp = models.ForeignKey(tally_group,on_delete = models.CASCADE,null = True)
    mname = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    pincode = models.CharField(max_length=6,null=True)
    bank_details = models.CharField(max_length=20,null=True)
    pan_no = models.CharField(max_length=100,null=True)
    registration_type = models.CharField(max_length=100,null=True)
    gst_uin = models.CharField(max_length=100,null=True)
    set_alter_gstdetails = models.CharField(max_length=100,null=True)
    opening_blnc = models.IntegerField(null=True)

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
    
    type_of_ledger = models.CharField(max_length=100,null=True)
    rounding_method = models.CharField(max_length=100,null=True)
    rounding_limit = models.IntegerField(blank=True, null=True, default=None)

    type_duty_tax = models.CharField(max_length=100,null=True)
    tax_type = models.CharField(max_length=100,null=True)
    valuation_type = models.CharField(max_length=100,null=True)
    rate_per_unit = models.IntegerField(blank=True, null=True, default=None)
    percentage_of_calcution = models.CharField(max_length=100,null=True)
    rond_method = models.CharField(max_length=100,null=True)
    rond_limit = models.IntegerField(blank=True, null=True, default=None)

    gst_applicable = models.CharField(max_length=100,null=True)
    setalter_gstdetails = models.CharField(max_length=20,null=True)
    type_of_supply = models.CharField(max_length=100,null=True)
    assessable_value = models.CharField(max_length=100,null=True)
    appropriate_to = models.CharField(max_length=100,null=True)
    method_of_calculation = models.CharField(max_length=100,null=True)

    balance_billbybill = models.CharField(max_length=100,null=True)
    credit_period = models.CharField(max_length=100,null=True)
    creditdays_voucher = models.CharField(max_length=100,null=True)

class ledger_cheque_demension(models.Model):
    cheque_width = models.IntegerField(null=True)
    cheque_height = models.IntegerField(null=True)
    startL_leftEdge = models.IntegerField(null=True)
    startL_topEdge = models.IntegerField(null=True)
    distancel_leftEdge = models.IntegerField(null=True)
    distancel_topEdge = models.IntegerField(null=True)
    date_style = models.CharField(max_length=100,null=True)
    date_seperator = models.CharField(max_length=10,null=True)
    separator_width = models.IntegerField(null=True)
    character_distance = models.FloatField(null=True)
    Pdistancel_leftEdge = models.IntegerField(null=True)
    Pdistancel_topEdge = models.IntegerField(null=True)
    area_width = models.IntegerField(null=True)
    secondL_DTE = models.IntegerField(null=True)
    secondfirstL_height = models.IntegerField(null=True)
    firstL_dTE = models.IntegerField(null=True)
    sl_fisrtl_LE = models.IntegerField(null=True)
    sl_secondl_LE = models.IntegerField(null=True)
    amount_widtharea = models.IntegerField(null=True)
    currencyFNM_print = models.CharField(max_length=10,null=True)
    df_TE = models.IntegerField(null=True)
    startL_LE = models.IntegerField(null=True)
    amt_widtharea = models.IntegerField(null=True)
    currencyS_print = models.CharField(max_length=10,null=True)
    company_name = models.CharField(max_length=10,null=True)
    print_CN = models.CharField(max_length=10,null=True)
    salutation_Fsign = models.CharField(max_length=100,null=True)
    salutation_Ssign = models.CharField(max_length=100,null=True)
    top_Edistance = models.IntegerField(null=True)
    startLF_leftE = models.IntegerField(null=True)
    width_sign_area = models.IntegerField(null=True)
    height_sign_area = models.IntegerField(null=True)

class ledger_bankdetails(models.Model):
    transaction_type = models.CharField(max_length=100)
    cross_using = models.CharField(max_length=100)
    acc_no = models.CharField(max_length=100)
    ifsc_code = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)

class ledger_chequebook(models.Model):
    from_number = models.IntegerField()
    to_number = models.IntegerField()
    no_of_cheques = models.IntegerField()
    cheque_bookname = models.CharField(max_length=100)

class ledger_gstvalues(models.Model):
    nature_of_transaction = models.CharField(max_length=255)
    taxable = models.CharField(max_length=100,null=True)
    taxability = models.CharField(max_length=100,null=True)
    appicable_from = models.DateField(null=True)
    integrated_tax = models.CharField(max_length=100,null=True)
    cess = models.CharField(max_length=100,null=True)

class voucher_advanceconf(models.Model):
    starting_no = models.IntegerField()
    numerical_partwidth = models.IntegerField()
    prefill_zero = models.CharField(max_length=10)
    restart_applicable_dt = models.DateField()
    restart_startingno = models.IntegerField()
    restart_particular = models.CharField(max_length=100)
    prefix_applicable_dt = models.DateField()
    prefix_particular = models.CharField(max_length=100)
    suffix_applicable_dt = models.DateField()
    suffix_particular = models.CharField(max_length=100)

class ledger_taxreggst(models.Model):
    registration_type = models.CharField(max_length=255)
    assessee_teritory = models.CharField(max_length=10)
    commerce_operator = models.CharField(max_length=10)
    party_deemed = models.CharField(max_length=10)
    party_type = models.CharField(max_length=100)
    gstin_uin = models.CharField(max_length=100)
    transporter = models.CharField(max_length=10)
    transporter_id = models.CharField(max_length=100,null=True)
