from pyexpat import model
from django.db import models

# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20)
    formal_name = models.CharField(max_length=20)
    fin_begin = models.DateField()
    books_begin = models.DateField()
    fin_end = models.DateField()
    status=models.BooleanField(default=True)

class Features(models.Model):
    maintain_accounts = models.CharField(max_length=10)
    bill_wise_entry = models.CharField(max_length=10)
    cost_centres = models.CharField(max_length=10)
    interest_calc = models.CharField(max_length=10)
    maintain_inventory = models.CharField(max_length=10)
    integrate_accounts = models.CharField(max_length=10)
    multiple_price_level = models.CharField(max_length=10)
    batches = models.CharField(max_length=10)
    expirydate_batches = models.CharField(max_length=10)
    joborder_processing = models.CharField(max_length=10)
    cost_tracking = models.CharField(max_length=10)
    job_costing= models.CharField(max_length=10)
    discount_invoices = models.CharField(max_length=10)
    Billed_Quantity = models.CharField(max_length=10)
    gst = models.CharField(max_length=10)
    tds = models.CharField(max_length=10)
    tcs = models.CharField(max_length=10)
    vat = models.CharField(max_length=10)
    excise = models.CharField(max_length=10)
    servicetax = models.CharField(max_length=10)
    payroll = models.CharField(max_length=10)
    multiple_addrss = models.CharField(max_length=10)
    vouchers = models.CharField(max_length=10)
    company=models.ForeignKey(Companies,on_delete = models.CASCADE,null = True)

class GST(models.Model):
    state = models.CharField(max_length=255,null=True)
    reg_type = models.CharField(max_length=50,null=True)
    assessee = models.CharField(max_length=50,null=True)
    gst_applicable = models.CharField(max_length=50,null=True)
    gstin = models.CharField(max_length=100,null=True)
    periodicity = models.CharField(max_length=50,null=True)
    flood_cess = models.CharField(max_length=20,null=True)
    applicable_from = models.CharField(max_length=50,null=True)
    gst_rate_details = models.CharField(max_length=20,null=True)
    advance_receipts = models.CharField(max_length=20,null=True)
    reverse_charge = models.CharField(max_length=20,null=True)
    gst_classification = models.CharField(max_length=20,null=True)
    bond_details = models.CharField(max_length=20,null=True)
    tax_rate = models.CharField(max_length=20,null=True)
    tax_calc = models.CharField(max_length=100,null=True)
    tax_purchase = models.CharField(max_length=20,null=True)
    
    eway_bill = models.CharField(max_length=20,null=True)
    applicable_form = models.CharField(max_length=50,null=True)
    threshold_includes = models.CharField(max_length=255,null=True)
    threshold_limit = models.CharField(max_length=100,null=True)
    intrastate = models.CharField(max_length=20,null=True)
    threshold_limit2 = models.CharField(max_length=100,null=True)
    print_eway = models.CharField(max_length=20,null=True)

    e_invoice = models.CharField(max_length=20,null=True)
    app_from = models.CharField(max_length=50,null=True)
    billfrom_place = models.CharField(max_length=50,null=True)
    dperiod = models.CharField(max_length=50,null=True)
    send_ewaybill = models.CharField(max_length=50,null=True)
    company=models.ForeignKey(Companies,on_delete = models.CASCADE,null = True)
    
class gst_lutbond(models.Model):
    lutbond = models.CharField(max_length=50)
    validity_from = models.DateField()
    validity_to = models.DateField()  

class gst_taxability(models.Model):
    taxability = models.CharField(max_length=50)
    applicable_dt = models.CharField(max_length=50,null=True)
    integrated_tax = models.CharField(max_length=50)
    cess = models.CharField(max_length=50)
    flood_cess = models.CharField(max_length=50)
    company=models.ForeignKey(Companies,on_delete = models.CASCADE,null = True) 

class Tds_Details(models.Model):
    tan_regno = models.CharField(max_length=40)
    tan = models.CharField(max_length=40)
    deductor_type = models.CharField(max_length=100)
    deductor_branch = models.CharField(max_length=255)
    person_details = models.CharField(max_length=255)
    ignore_it = models.CharField(max_length=40)
    active_tds = models.CharField(max_length=40)
    company=models.ForeignKey(Companies,on_delete = models.CASCADE,null = True)

class tds_person(models.Model):
    name = models.CharField(max_length=255,null=True)
    son_daughter = models.CharField(max_length=255,null=True)
    designation = models.CharField(max_length=255,null=True)
    pan = models.CharField(max_length=255,null=True)
    flat_no = models.CharField(max_length=10,null=True)
    building = models.CharField(max_length=255,null=True)
    street = models.CharField(max_length=100,null=True)
    area = models.CharField(max_length=100,null=True)
    town = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=255,null=True)
    pincode = models.CharField(max_length=10,null=True)
    mobile = models.CharField(max_length=15,null=True)
    std = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=10,null=True)
    email = models.EmailField(null=True)
    company=models.ForeignKey(Companies,on_delete = models.CASCADE,null = True) 

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

class currencyAlteration(models.Model):
    Symbol = models.CharField(max_length=255)
    FormalName = models.CharField(max_length=255)
    ISOCurrency = models.CharField(max_length=30,null=True)
    DecimalPlace = models.IntegerField()
    showAmount = models.CharField(max_length=20)
    suffixSymbol = models.CharField(max_length=20)
    AddSpace = models.CharField(max_length=20)
    wordRep = models.CharField(max_length=255,null=True)
    DecimalWords = models.IntegerField()

class company_alt_currency(models.Model):
    c_symbol = models.CharField(max_length=255)
    formal_name = models.CharField(max_length=255)
    iso_Ccode = models.CharField(max_length=30,null=True)
    decimal_place = models.IntegerField()
    show_amtM = models.CharField(max_length=20)
    suffix_smblA = models.CharField(max_length=20)
    add_space = models.CharField(max_length=20)
    word_rep = models.CharField(max_length=255,null=True)
    no_decimal = models.IntegerField()

class rateofexchange(models.Model):
    date_ROE = models.DateField(null=True)
    currencyName =models.CharField(max_length=100, null=True)
    std_rate = models.CharField(max_length=100, null=True)
    sell_voucher_rate = models.CharField(max_length=100, null=True)
    sell_specified_rate = models.CharField(max_length=100, null=True)
    buy_specified_rate = models.CharField(max_length=100, null=True)
    buy_voucher_rate = models.CharField(max_length=100, null=True)
    currencyAlteration=models.ForeignKey(currencyAlteration, on_delete=models.CASCADE, null=True)

class cost_centre(models.Model):
    cname=models.CharField(max_length=255)
    cost_alias = models.CharField(max_length=255)
    under = models.CharField(max_length=255)

class Voucher(models.Model):
    voucher_name = models.CharField(max_length=255,null=True)
    alias = models.CharField(max_length=255,null=True)
    voucher_type = models.CharField(max_length=255,null=True)
    abbreviation = models.CharField(max_length=255,null=True)
    voucherActivate = models.CharField(max_length=20,null=True)
    voucherNumber = models.CharField(max_length=200,null=True)
    preventDuplicate = models.CharField(max_length=20,null=True)
    advance_con = models.CharField(max_length=20,null=True)
    voucherEffective = models.CharField(max_length=20,null=True)
    transaction = models.CharField(max_length=20,null=True)
    make_optional = models.CharField(max_length=20,null=True)
    voucherNarration = models.CharField(max_length=20,null=True)
    provideNarration = models.CharField(max_length=20,null=True)
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

class bank_name(models.Model):
    bankname = models.CharField(max_length=100,null=True)

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

#============================ Aswathy Work ===================================

class revised_applicability(models.Model):
    appl_from=models.CharField(max_length=100)

class revised_applicability_composition(models.Model):
    appl_from_c=models.CharField(max_length=100)

class stockgroupcreation(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under=models.CharField(max_length=100)
    quantities=models.CharField(max_length=100)
    
class stockcatagorycreation(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under=models.CharField(max_length=100)

class CreateGodown(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)

class Price_level(models.Model):
    number=models.CharField(max_length=255,null=True)

class pancin(models.Model):
    pan=models.CharField(max_length=30)
    cin=models.CharField(max_length=30)

class unit_simple(models.Model):
    type=models.CharField(max_length=100)
    symbol=models.CharField(max_length=100)
    formal_name=models.CharField(max_length=100)
    uqc=models.CharField(max_length=100)
    decimal=models.IntegerField()
    
class unit_compound(models.Model):
    typ=models.CharField(max_length=100)
    f_unit=models.CharField(max_length=100,null=True)
    conversion=models.IntegerField()
    s_unit=models.CharField(max_length=100,null=True)

class uqcs(models.Model):
    uqc_name=models.CharField(max_length=100)

class stock_item(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under=models.CharField(max_length=100,null=True)
    units=models.CharField(max_length=100,null=True)
    batches=models.CharField(max_length=10,null=True)
    cost_tracking=models.CharField(max_length=10,null=True)
    gst_applicable=models.CharField(max_length=100,null=True)
    typ_sply=models.CharField(max_length=100)
    set_alter=models.CharField(max_length=100)
    rate_of_duty=models.IntegerField()
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)
    
class gst_stockitem(models.Model):
    calc_typ=models.CharField(max_length=100)
    taxability=models.CharField(max_length=100)
    tax=models.CharField(max_length=100)
    cess=models.CharField(max_length=100)


