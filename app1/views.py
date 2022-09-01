import datetime
from datetime import timedelta
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def base(request):
    return render(request, 'base.html')

def demo(request):
    return render(request, 'demo.html')


#......................jisha........................

def company_list(request):
    com=Companies.objects.all()
    return render(request,'company_list.html',{'comp':com})    

def change_company(request):
	com=Companies.objects.all()
	return render(request, 'change_company.html',{'comp':com})

def select_c(request):
	com = Companies.objects.all()
	return render(request,'select_c.html',{'com':com})

def shut_cmpny(request):
	com=Companies.objects.all() 
	return render(request, 'shut_cmpny.html',{'com':com})

def shut(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('shut_cmpny') 

def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=True
    c.save()
    return redirect('shut_cmpny')

def ledgers(request):
	grp=tally_group.objects.all()
	com=Companies.objects.filter(status=True) 
	return render(request,'ledgers.html',{'grp' : grp,'com':com})

def vouchers(request):
	com=Companies.objects.filter(status=True) 
	return render(request, 'vouchers.html',{'com':com})

def groups(request):
	com=Companies.objects.filter(status=True) 
	return render(request, 'group.html',{'com':com})

def group_alt(request):
    return render(request, 'group_alt.html')

def currency(request):
    return render(request, 'currency.html')

def c_create(request):
    return render(request, 'c_create.html')

def c_alter(request):
    return render(request, 'c_alter.html')

def cost(request):
	costt=cost_centre.objects.all()
	return render(request,'cost.html',{'costt' : costt})

def cost_alt(request):
	costt=cost_centre.objects.all()
	return render(request, 'cost_alt.html',{'costt' : costt})

def create_cmpny(request):
    return render(request, 'create_cmpny.html')

def tally_gst(request,pk):
	company=Companies.objects.get(id=pk)
	return render(request, 'gst.html',{'company':company})

def gst_tax(request,pk):
	company=Companies.objects.get(id=pk)
	return render(request, 'gst_tax.html',{'company':company})

def features(request):
	return render(request, 'features.html')

def tds(request,pk):
	comp=Companies.objects.get(id=pk)
	return render(request, 'tds.html',{'company':comp})    

def person(request,pk):
	comp=Companies.objects.get(id=pk)
	return render(request, 'tds_person.html',{'company':comp})

def lut_bond(request):
    return render(request, 'lut_bond.html')

def cheque(request):
    return render(request, 'cheque.html')

def ledger_gst(request):
    return render(request, 'ledger_gst.html')

def ledger_chequed(request):
    return render(request, 'ledger_chequed.html')

def vouch_advance(request):
    return render(request, 'vouch_advance.html')

def ledger_taxgst(request):
    return render(request, 'ledger_taxgst.html')

def b_name(request):
	comp=Companies.objects.all()
	return render(request,'bankname.html',{'comp':comp})

def create_group(request):
	if request.method=='POST':
		gname=request.POST['gname']
		galias=request.POST['alias']
		under=request.POST['group']
		nature=request.POST['group_nature']
		gross=request.POST['gorss_profit']
		ledg=request.POST['ledger']
		cred=request.POST['debit/credit']
		calc=request.POST['calculation']
		invc=request.POST['invoice']
		grp=tally_group(group_name=gname,
                group_alias=galias,
                group_under=under,
                nature=nature,
                gross_profit=gross,
                sub_ledger=ledg,
                debit_credit=cred,
                calculation=calc,
                invoice=invc,
                )          
		grp.save()
		print("added")
		return redirect('/')

def create_currency(request):
	if request.method=='POST':
		smbl=request.POST['c_symbl']
		fname=request.POST['fname']
		isoc=request.POST['isocode']
		dcml=request.POST['decimal_p']
		amt=request.POST['show_amt']
		sfx=request.POST['suffix']
		spc=request.POST['add_space']
		wrd=request.POST['word_rep']
		ndcml=request.POST['no_decimal']
		crny=currencyAlteration(Symbol=smbl,
                        FormalName = fname,
                        ISOCurrency = isoc,
                        DecimalPlace = dcml,
                        showAmount = amt,
                        suffixSymbol = sfx,
                        AddSpace = spc,
                        wordRep = wrd,
                        DecimalWords = ndcml)          
		crny.save()
		print("added")
		return redirect('/')

def rates(request):
	curcc = currencyAlteration.objects.all()
	return render(request,'rates.html',{'curcc':curcc})

def create_ROE(request):
    if request.method=='POST':
        curncy=request.POST['curname']
        cstdrate=request.POST['stdr']
        
        csrate=request.POST['sr']
        
        bsrate=request.POST['sr2']
        raex=rateofexchange(
                        
                          std_rate=cstdrate,
                        
                          sell_specified_rate=csrate,
                        
                          buy_specified_rate=bsrate,
                          currencyName=curncy,
						  )
        raex.save()
        print("added")
        return redirect('rates')
    return render(request,'rates.html')

# def create_ROE(request):
# 	if request.method=='POST':
# 		dt=request.POST['dt']
# 		crname=request.POST['curname']
# 		stdr=request.POST['stdr']
# 		lv=request.POST['lvr']
# 		ssr=request.POST['ssr']
# 		lv1=request.POST['lvr2']
# 		bsr=request.POST['bsr']
# 		croe=rateofexchange(date_ROE=dt,
#                         currencyName = crname,
#                         std_rate = stdr,
#                         sell_voucher_rate = lv,
#                         sell_specified_rate = ssr,
# 						buy_specified_rate = lv1,
#                         buy_voucher_rate = bsr)          
# 		croe.save()
# 		print("added")
# 		return redirect('/')
# 	return render(request,'rates.html')

def alter_currency(request):
	if request.method=='POST':
		smbl=request.POST['c_symbl']
		fname=request.POST['fname']
		isoc=request.POST['isocode']
		dcml=request.POST['decimal_p']
		amt=request.POST['show_amt']
		sfx=request.POST['suffix']
		spc=request.POST['add_space']
		wrd=request.POST['word_rep']
		ndcml=request.POST['no_decimal']
		crny=company_alt_currency(c_symbol=smbl,
                        formal_name = fname,
                        iso_Ccode = isoc,
                        decimal_place = dcml,
                        show_amtM = amt,
                        suffix_smblA = sfx,
                        add_space = spc,
                        word_rep = wrd,
                        no_decimal = ndcml)          
		crny.save()
		print("added")
		return redirect('/')

def load_centre(request):
	costt=cost_centre.objects.all()
	if request.method=='POST':
		nm=request.POST['cst_name']
		als=request.POST['alias']
		unr=request.POST['c_under']
		cost=cost_centre(cname=nm,
                        cost_alias = als,
                        under = unr)          
		cost.save()
		print("added")
		return redirect('load_centre')
	return render(request,'cost.html',{'costt':costt})
		

def create_tds(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		t_reg = request.POST['tan_reg_no']
		tax_clct = request.POST['tax_ded_clctn']
		ded_type = request.POST['deductor_type']
		ded_bd = request.POST['ded_brachdevision']
		prsn_res = request.POST['person_res']
		ignr = request.POST['ignore_it']
		st_itm = request.POST['tds_stock_items']
		
		ctds=Tds_Details(tan_regno=t_reg,
                        tan = tax_clct,
                        deductor_type = ded_type,
                        deductor_branch = ded_bd,
                        person_details = prsn_res,
                        ignore_it = ignr,
                        active_tds = st_itm,
						company = id)          
		ctds.save()
		print("added")
		return redirect('/')
	return render(request,'tds.html')

def person_tds(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		name = request.POST['name']
		sd = request.POST['son_daughter']
		des = request.POST['designation']
		pan = request.POST['pan']
		ftno = request.POST['flat_no']
		pnm = request.POST['premise_name']
		str = request.POST['street']
		are = request.POST['area']
		city = request.POST['city']
		st = request.POST['state']
		pcd = request.POST['pincode']
		m_no = request.POST['mobile_no']
		std = request.POST['std_code']
		tph = request.POST['telephone']
		emal = request.POST['email']
	    
		prs=tds_person(name=name,
                        son_daughter = sd,
                        designation = des,
                        pan = pan,
                        flat_no = ftno,
                        building = pnm,
                        street = str,
                        area = are,
                        town = city,
                        state = st,
                        pincode = pcd,
                        mobile = m_no,
                        std = std,
                        telephone = tph,
                        email = emal,
						company = id)          
		prs.save()
		print("added")
		return redirect('/')
	return render(request,'tds_person.html')

def create_voucher(request):
	if request.method=='POST':
		nm=request.POST['vname']
		als=request.POST['alias']
		vtp=request.POST['vouch_type']
		abbr=request.POST['Abbreviation']
		actp=request.POST['activate_Vtype']
		mvno=request.POST['method_Vno']
		prnt=request.POST['prevent']
		acn=request.POST['advance_con']
		use=request.POST['use_EDV']
		zero=request.POST['zero_val']
		mvd=request.POST['mVoptional_defualt']
		anar=request.POST['allow_nar']
		prvdl=request.POST['provide_L']
		jrnl=request.POST['manu_jrnl']
		track=request.POST['track_purchase']
		enbl=request.POST['enable_acc']
		prntva=request.POST['prnt_VA_save']
		prntfml=request.POST['prnt_frml']
		juri=request.POST['jurisdiction']
		tprint=request.POST['title_print']
		setaltr=request.POST['set_alter']
		posinv=request.POST['pos_invoice']
		msg1=request.POST['msg_1']
		msg2=request.POST['msg_2']
		dbank=request.POST['default_bank']
		nc=request.POST['name_class']

		vhr=Voucher(voucher_name=nm,
                    alias = als,
                    voucher_type = vtp,
                    abbreviation = abbr,
                    voucherActivate = actp,
                    voucherNumber = mvno,
                    preventDuplicate = prnt,
                    advance_con = acn,
                    voucherEffective = use,
                    transaction = zero,
                    make_optional = mvd,
                    voucherNarration = anar,
                    provideNarration = prvdl,
                    manu_jrnl = jrnl,
                    track_purchase = track,
                    enable_acc = enbl,
                    prnt_VA_save = prntva,
                    prnt_frml = prntfml,
                    jurisdiction = juri,
                    title_print = tprint,
                    set_alter = setaltr,
                    pos_invoice = posinv,
                    msg_1 = msg1,
                    msg_2 = msg2,
                    default_bank = dbank,
                    name_class = nc)          
		vhr.save()
		print("Added")
		return redirect('/')



def create_gst(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		st = request.POST['state']
		rt = request.POST['registration_type']
		at = request.POST['assessee_territory']
		gsta = request.POST['gst_applicable']
		gstuin = request.POST['gstin_uin']
		prd = request.POST['periodicity']

	# .................regular.................

		kfca = request.POST['kerala_fca']
		af = request.POST['applicable_from']
		gstrd = request.POST['gst_rate_details']
		tla = request.POST['tl_advanceR']
		tlr = request.POST['tl_reverseC']
		gstc = request.POST['gst_classification'] 
		lb = request.POST['lut_bond']

    # ................composition................  
	  
		tr = request.POST['tax_rate']
		tc = request.POST['tax_calculation']
		tp = request.POST['tax_purchase']

	# ............e-Way bill applicable...........

		ea = request.POST['e_waybillA']
		aaf = request.POST['applicable_f']
		tli = request.POST['thresholdlimit_include']
		tl = request.POST['threshold_limit']
		intr = request.POST['intrastate']
		itl = request.POST['ithreshold_limit']
		pnw = request.POST['print_eway']

	# .............e-Invoice applicable..............

		einva = request.POST['e_invoiceA']
		appf = request.POST['app_f']
		bfp = request.POST['billfrom_place']
		peir = request.POST['period_einvoiceR']
		sewdei = request.POST['send_eW_details_einvoice']
        
		gstd=GST(state=st,
						reg_type=rt,
						assessee=at,
						gst_applicable=gsta,
						gstin=gstuin,
						periodicity=prd,
					# ........regular.......
						flood_cess=kfca,
						applicable_from=af,
						gst_rate_details=gstrd,
						advance_receipts=tla,
						reverse_charge=tlr,
						gst_classification=gstc,
						bond_details=lb,	
					# ........composition.......
						tax_rate=tr,		
						tax_calc=tc,		
						tax_purchase=tp,
					# ........e-Way bill applicable.......
						eway_bill=ea,
						applicable_form=aaf,
						threshold_includes=tli,
						threshold_limit=tl,
						intrastate=intr,
						threshold_limit2=itl,
						print_eway=pnw,
					# ........e-Invoice applicable.......
						e_invoice=einva,
						app_from=appf,
						billfrom_place=bfp,
						dperiod=peir,
						send_ewaybill=sewdei,
						company=id)
		gstd.save()
		print("Added")
		return redirect('/')
	return render(request,'gst.html')

def create_gsttax(request,pk):
	id=Companies.objects.get(id=pk)
	if request.method=='POST':
		txb=request.POST['taxability']
		af=request.POST['appicable_from']
		it=request.POST['integrated_tax']
		ces=request.POST['cess']
		fc=request.POST['flood_cess']
		
		cost=gst_taxability(taxability=txb,
                        applicable_dt = af,
                        integrated_tax = it,      
                        cess = ces,      
                        flood_cess = fc,
						company = id)          
		cost.save()
		print("Added")
		return redirect('/')
	return render(request,'gst_tax.html')

def create_lutbond(request):
	if request.method=='POST':
		lbno=request.POST['lut_bondNo']
		afrom=request.POST['application_from']
		ato=request.POST['application_to']
		lb=gst_lutbond(lutbond=lbno,
                        validity_from = afrom,
                        validity_to = ato)      
		lb.save() 
		print("Added")
		return redirect('lut_bond')
	return render(request,'lut_bond')

def create_ledger(request):
    if request.method=='POST':
        nm=request.POST.get('name')
        als=request.POST.get('alias')
        under=request.POST.get('under')
        mname=request.POST.get('mailingname')
        adr=request.POST.get('address')
        st=request.POST.get('state')
        cntry=request.POST.get('country')
        pin=request.POST.get('pincode')
        pno=request.POST.get('pan_no')
        bdetls=request.POST.get('bank_details')
        rtype=request.POST.get('registration_type')
        gst_uin=request.POST.get('gst_uin')
        opnbn=request.POST.get('opening_blnc')

        spdl=request.POST.get('set_odl')
        achnm=request.POST.get('ac_holder_nm')
        acno=request.POST.get('acc_no')
        ifsc=request.POST.get('ifsc_code')
        scode=request.POST.get('swift_code')
        bn=request.POST.get('bank_name')
        brnch=request.POST.get('branch')
        sacbk=request.POST.get('SA_cheque_bk')
        ecp=request.POST.get('Echeque_p')
        sacpc=request.POST.get('SA_chequeP_con')

        typofled=request.POST.get('type_of_ledger')
        rometh=request.POST.get('rounding_method')
        rolmt=request.POST.get('rounding_limit')

        typdutytax=request.POST.get('type_duty_tax')
        taxtyp=request.POST.get('tax_type')
        valtype=request.POST.get('valuation_type')
        rateperu=request.POST.get('rate_per_unit')
        percalc=request.POST.get('percentage_of_calcution')
        rondmethod=request.POST.get('rond_method')
        roimlit=request.POST.get('rond_limit')

        gstapplicbl=request.POST.get('gst_applicable')
        sagatdet=request.POST.get('setalter_gstdetails')
        typsupply=request.POST.get('type_of_supply')
        asseval=request.POST.get('assessable_value')
        appropto=request.POST.get('appropriate_to')
        methcalcu=request.POST.get('method_of_calculation')

        balbillbybill=request.POST.get('balance_billbybill')
        credperiod=request.POST.get('credit_period')
        creditdaysvouch=request.POST.get('creditdays_voucher')
        
        ldr=tally_ledger(name=nm,alias=als,under=under,mname=mname,address=adr,state=st,country=cntry,
						pincode=pin,pan_no=pno,bank_details=bdetls,registration_type=rtype,gst_uin=gst_uin,
						opening_blnc=opnbn,set_odl=spdl,ac_holder_nm=achnm,acc_no=acno,ifsc_code=ifsc,swift_code=scode,
						bank_name=bn,branch=brnch,SA_cheque_bk=sacbk,Echeque_p=ecp,SA_chequeP_con=sacpc,
						type_of_ledger=typofled,rounding_method=rometh,rounding_limit=rolmt,type_duty_tax=typdutytax,tax_type=taxtyp,
						valuation_type=valtype,rate_per_unit=rateperu,percentage_of_calcution=percalc,rond_method=rondmethod,rond_limit=roimlit,
						gst_applicable=gstapplicbl,setalter_gstdetails=sagatdet,type_of_supply=typsupply,assessable_value=asseval,
						appropriate_to=appropto,method_of_calculation=methcalcu,balance_billbybill=balbillbybill,credit_period=credperiod,
						creditdays_voucher=creditdaysvouch)
		
        ldr.save()
        return render(request,'ledgers.html')

def create_ledgerdimension(request):
	if request.method == 'POST':
		cw= request.POST.get('cheque_width')
		ch= request.POST.get('cheque_height')
		sle= request.POST.get('startL_leftEdge')
		slte= request.POST.get('startL_topEdge')
		dlle= request.POST.get('distancel_leftEdge')
		dlte= request.POST.get('distancel_topEdge')
		ds= request.POST.get('date_style')
		dts= request.POST.get('date_seperator')
		sw= request.POST.get('separator_width')
		cd= request.POST.get('character_distance')
		pdle= request.POST.get('Pdistancel_leftEdge')
		pdlte= request.POST.get('Pdistancel_topEdge')
		aw= request.POST.get('area_width')
		sldte= request.POST.get('secondL_DTE')
		sflh= request.POST.get('secondfirstL_height')
		fldte= request.POST.get('firstL_dTE')
		slfle= request.POST.get('sl_fisrtl_LE')
		slsle= request.POST.get('sl_secondl_LE')
		awa= request.POST.get('amount_widtharea')
		cfnmp= request.POST.get('currencyFNM_print')
		dfte= request.POST.get('df_TE')
		sle= request.POST.get('startL_LE')
		amwa= request.POST.get('amt_widtharea')
		csp= request.POST.get('currencyS_print')
		cn= request.POST.get('company_name')
		pcn= request.POST.get('print_CN')
		sfs= request.POST.get('salutation_Fsign')
		sss= request.POST.get('salutation_Ssign')
		tes= request.POST.get('top_Edistance')
		slfl= request.POST.get('startLF_leftE')
		wsa= request.POST.get('width_sign_area')
		hsa= request.POST.get('height_sign_area')

		cld= ledger_cheque_demension(cheque_width=cw,cheque_height=ch,startL_leftEdge=sle,startL_topEdge=slte,distancel_leftEdge=dlle,
									distancel_topEdge=dlte,date_style=ds,date_seperator=dts,separator_width=sw,character_distance=cd,
									Pdistancel_leftEdge=pdle,Pdistancel_topEdge=pdlte,area_width=aw,secondL_DTE=sldte,secondfirstL_height=sflh,
									firstL_dTE=fldte,sl_fisrtl_LE=slfle,sl_secondl_LE=slsle,amount_widtharea=awa,currencyFNM_print=cfnmp,
									df_TE=dfte,startL_LE=sle,amt_widtharea=amwa,currencyS_print=csp,company_name=cn,print_CN=pcn,
									salutation_Fsign=sfs,salutation_Ssign=sss,top_Edistance=tes,startLF_leftE=slfl,width_sign_area=wsa,
									height_sign_area=hsa)

		cld.save()
		return redirect('/')
	return render(request,'ledger_chequed.html')

def company_create(request):
	if request.method=="POST":
		name=request.POST['companyname']
		mname=request.POST['mailing_name']
		addr=request.POST['address']
		st=request.POST['state']
		cntry=request.POST['country']
		pncd=request.POST['pincode']
		tlphn=request.POST['telephone']
		mbl=request.POST['mobile']
		fax=request.POST['fax']
		email=request.POST['email']
		wbsit=request.POST['website']
		fin_begin=request.POST['fyear']
		bk_begin=request.POST['byear']
		crny_symbol=request.POST['currency']
		frml_name=request.POST['formal']

		ccmp=Companies.objects.filter(name=name)
		out=datetime.datetime.strptime (fin_begin,'%Y-%m-%d')+timedelta (days=364) 
		a=out.date()
		

		if ccmp:
			messages.info(request,'Company name already exists!!')
			return redirect('create_cmpny')
		else:
			cmp=Companies(name=name,mailing_name=mname,address=addr,state=st,country=cntry,
                pincode=pncd,telephone=tlphn,mobile=mbl,fax=fax,email=email,website=wbsit,fin_begin=fin_begin,
                books_begin=bk_begin,currency_symbol=crny_symbol,formal_name=frml_name,fin_end=a)
			cmp.save()
			messages.info(request,'Company created successfully(Enable the features as per your business needs)')
			return render(request,'features.html',{'cmp':cmp})

def company_feature(request,cf):
	id=Companies.objects.get(id=cf)
	if request.method=="POST":
		ma=request.POST['maintain_account']
		be=request.POST['billwise_entry']
		cc=request.POST['cost_centre']
		ic=request.POST['interest_calculation']
		mi=request.POST['maintain_inventry']
		ai=request.POST['account_inventry']
		mpl=request.POST['multiple_pricelevel']
		eb=request.POST['enable_batches']
		edt=request.POST['expiry_date']
		jop=request.POST['job_order_procress']
		ct=request.POST['cost_tracking']
		jc=request.POST['job_costing']
		dc=request.POST['discount_column']
		sa=request.POST['seperte_actual']
		gst=request.POST['gst']
		tds=request.POST['tds']
		tcs=request.POST['tcs']
		vat=request.POST['vat']
		excise=request.POST['excise']
		st=request.POST['service_tax']
		prl=request.POST['payroll']
		maddr=request.POST['multiple_address']
		mark_mod=request.POST['mark_modified']

		cmp_fet=Features(maintain_accounts=ma,bill_wise_entry=be,cost_centres=cc,interest_calc=ic,maintain_inventory=mi,
		integrate_accounts=ai,multiple_price_level=mpl,batches=eb,expirydate_batches=edt,joborder_processing=jop,cost_tracking=ct,job_costing=jc,discount_invoices=dc,
		Billed_Quantity=sa,gst=gst,tds=tds,tcs=tcs,vat=vat,excise=excise,servicetax=st,payroll=prl,multiple_addrss=maddr,
		vouchers=mark_mod,company=id)

		cmp_fet.save()
		return redirect('/')
	return render(request,'features.html',{'cmp':id})

def bank_details(request):
	bn = bank_name.objects.all()
	return render(request,'bank_details.html',{'bn' : bn})
	
def create_bankdetails(request):
	if request.method=='POST':
		transaction_type=request.POST['transaction_type']
		acp=request.POST['ac_payee']
		acc_no=request.POST['acc_no']
		ifsc_code=request.POST['ifsc_code']
		bank_name=request.POST['bank_name']
		lbd=ledger_bankdetails(transaction_type=transaction_type,
                        cross_using = acp,
                        acc_no = acc_no,      
                        ifsc_code = ifsc_code,      
                        bank_name =bank_name)      
		lbd.save() 
		print("Added")
		return redirect('bank_details')
	return render(request,'bank_details.html')


def bankname(request):
	if request.method=='POST':
		bn = request.POST['bank_name']
		bnn=bank_name(bankname = bn)
		bnn.save()
		return redirect('bankname')
	return render(request,'bankname.html')


def create_chequebk(request):
	if request.method=='POST':
		fn=request.POST['from_number']
		tn=request.POST['to_number']
		nc=request.POST['number_cheques']
		nmc=request.POST['name_chequebk']
		lcb=ledger_chequebook(from_number=fn,
                        to_number = tn,
                        no_of_cheques = nc,
                        cheque_bookname = nmc)      
		lcb.save() 
		print("Added")
		return redirect('cheque')
	return render(request,'cheque.html')

def create_ledger_gst(request):
	if request.method=='POST':
		ntrot=request.POST['nature_of_transaction']
		txbl=request.POST['taxable']
		txblty=request.POST['taxability']
		aplifm=request.POST['appicable_from']
		inttx=request.POST['integrated_tax']
		ces=request.POST['cess']
		lgst=ledger_gstvalues(nature_of_transaction=ntrot,
                        taxable = txbl,
                        taxability = txblty,
                        appicable_from = aplifm,
                        integrated_tax = inttx,
                        cess = ces)    
		lgst.save()  
		print("Added")
		return redirect('ledger_gst')
	return render(request,'ledger_gst.html')

def create_voucher_advance(request):
	if request.method=='POST':
		stn=request.POST['starting_no']
		npw=request.POST['numerical_partwidth']
		pz=request.POST['prefill_zero']
		rsad=request.POST['restart_applicable_dt']
		rsrtsno=request.POST['restart_startingno']
		repert=request.POST['restart_particular']
		pread=request.POST['prefix_applicable_dt']
		preper=request.POST['prefix_particular']
		sfxapd=request.POST['suffix_applicable_dt']
		sfxper=request.POST['suffix_particular']

		cva=voucher_advanceconf(starting_no=stn,
                        numerical_partwidth = npw,
                        prefill_zero = pz,
                        restart_applicable_dt = rsad,
                        restart_startingno = rsrtsno,
                        restart_particular = repert,
                        prefix_applicable_dt = pread,
                        prefix_particular = preper,
                        suffix_applicable_dt = sfxapd,
                        suffix_particular = sfxper)    
		cva.save()  
		print("Added")
		return redirect('vouch_advance')
	return render(request,'vouch_advance.html')

def create_ledger_taxgst(request):
	if request.method=='POST':
		regtp=request.POST['registration_type']
		assester=request.POST['assessee_teritory']
		comop=request.POST['commerce_operator']
		partde=request.POST['party_deemed']
		partytyp=request.POST['party_type']
		gstinuin=request.POST['gstin_uin']
		transp=request.POST['transporter']
		transpid=request.POST['transporter_id']

		lgt=ledger_taxreggst(registration_type=regtp,
                        assessee_teritory = assester,
                        commerce_operator = comop,
                        party_deemed = partde,
                        party_type = partytyp,
                        gstin_uin = gstinuin,
                        transporter = transp,
                        transporter_id = transpid)    
		lgt.save()  
		print("Added")
		return redirect('ledger_taxgst')
	return render(request,'ledger_taxgst.html')

#================================ Aswathy Work (app views) ================================

def godown_alt(request):
	gd=CreateGodown.objects.all()
	return render(request,'godown_alt.html',{'gd':gd})

def stockgroup_alt(request):
	und=stockgroupcreation.objects.all()
	return render(request,'stockgroup_alt.html',{'und':und})

def stockcate_alt(request):
	cagy=stockgroupcreation.objects.all()
	return render(request,'stockcate_alt.html',{'cagy':cagy})

def unitcreate_alt(request):
    return render(request,'unitcreate_alt.html')

def load_stock_group(request):
	und=stockgroupcreation.objects.all()
	return render(request,'stock_group.html',{'und':und})

def stock_group(request):
	und=stockgroupcreation.objects.all()
	if request.method=='POST':
		name=request.POST['name']
		alias=request.POST['alias']
		under_name=request.POST['under_name']
		quantities=request.POST['quantities']
		stockgrp=stockgroupcreation(name=name,alias=alias,under=under_name,quantities=quantities)
		stockgrp.save()
		return redirect('stock_group')
	return render(request,'stock_group.html',{'und':und})

def load_stock_catagory(request):
	cagy=stockcatagorycreation.objects.all()
	return render(request,'stock_catagory.html',{'cagy':cagy})

def stock_catagory(request):
	cagy=stockcatagorycreation.objects.all()
	if request.method=='POST':
		name=request.POST['name']
		alias=request.POST['alias']
		under_name=request.POST['under_name']

		stockcagy=stockcatagorycreation(name=name,alias=alias,under=under_name)
		stockcagy.save()
		return redirect('stock_catagory')
	return render(request,'stock_catagory.html',{'cagy':cagy})

def load_unit_creation(request):
	u=uqcs.objects.all()
	return render(request,'unit_creation.html',{'u': u})

def unit_sim(request):
	u=uqcs.objects.all()
	if request.method=='POST':
		typ=request.POST['type']
		sym=request.POST['symb']
		formal_name=request.POST['fname']
		uqc=request.POST['uqc']
		decimal=request.POST['decimal']
		sim=unit_simple(type=typ,symbol=sym,formal_name=formal_name,uqc=uqc,decimal=decimal)
		sim.save()
		return redirect('unit_sim')
	return render(request,'unit_creation.html',{'u': u})

def new_uqcs(request):
	if request.method=='POST':
		uqc = request.POST['uqc_name']
		uq=uqcs(uqc_name = uqc)
		uq.save()
		return redirect('new_uqcs')
	return render(request,'unit_uqc.html')

def load_unit_compound(request):
    c=unit_simple.objects.all()
    return render(request,'unit_compound.html',{'c':c})

def unit_com(request):
    c=unit_simple.objects.all()
    if request.method=='POST':
        typ=request.POST['compound']
        con=request.POST['conversion']
        sunit=request.POST['s_unit']
        funit=request.POST['f_unit']
        comp=unit_compound(typ=typ,f_unit=funit,conversion=con,s_unit=sunit)
        comp.save()
        return redirect('unit_com')
    return render(request,'unit_compound.html',{'c':c})

def load_stock_item_creation(request):
    grp=stockgroupcreation.objects.all()
    unt=unit_compound.objects.all()
    u=unit_simple.objects.all()
    return render(request,'stock_item_creation.html',{'grp':grp,'unt':unt,'u':u})

def stock_items(request):
    grp=stockgroupcreation.objects.all()
    unt=unit_compound.objects.all()
    u=unit_simple.objects.all()
    if request.method=='POST':
        name1=request.POST['name1']
        alias=request.POST['alias']
        gst_applicable=request.POST['gst_applicable']
        set_alter=request.POST['set_alter']
        typ_sply=request.POST['typ_sply']
        rate_of_duty=request.POST['rate_of_duty']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        value=request.POST['value']
        funit2=request.POST['funit']
        
        e2=unit_compound.objects.get(id=funit2)
        gr=request.POST['name']
        e3=stockgroupcreation.objects.get(id=gr)
        crt=stock_item(name1=name1,alias=alias,typ_sply=typ_sply,gst_applicable=gst_applicable,set_alter=set_alter,
                           rate_of_duty=rate_of_duty,quantity=quantity,rate=rate,per=per,value=value,unit_compound=e2,stockgroupcreation=e3)
        crt.save()
        return redirect('stock_items')
    return render(request,'stock_item_creation.html',{'grp':grp,'unt':unt,'u':u})

def load_company_price(request):
    return render(request,'company_price.html')

def price_levels(request):
    price=Price_level.objects.all()
    if request.method=="POST":
        number=request.POST['number']
        crt=Price_level(number=number)
        crt.save()
        return redirect('price_levels')
    return render(request,'company_price.html')

def load_pan_cin(request):
    return render(request,'pan_cin.html')

def pan_cin(request):
    pc=pancin.objects.all()
    if request.method=='POST':
        pan=request.POST['pan']
        cin=request.POST['cin']
        crt=pancin(pan=pan,cin=cin)
        crt.save()
    return render(request,'pan_cin.html')

def godown_creation(request):
	gd=CreateGodown.objects.all()
	return render(request,'godown.html',{'gd':gd})

def godown(request):
	gd=CreateGodown.objects.all()
	if request.method=='POST':
		name=request.POST['name']
		alias=request.POST['alias']
		under_name=request.POST['under_name']
		gdcrt=CreateGodown(name=name,alias=alias,under_name=under_name)
		gdcrt.save()
		return redirect('godown')
	return render(request,'godown.html',{'gd':gd})

def load_rev(request):
    return render(request,'revised.html')

def revised(request):
    rev=revised_applicability.objects.all()
    if request.method=='POST':
        appl_from=request.POST['appl_from']
        r=revised_applicability(appl_from=appl_from)
        r.save()
        return redirect('revised')
    return render(request,'revised.html')

def load_rev_c(request):
    return render(request,'revised_composition.html')

def revised_composition(request):
    rev=revised_applicability_composition.objects.all()
    if request.method=='POST':
        appl_from_composition=request.POST['appl_from_composition']
        re=revised_applicability_composition(appl_from_c=appl_from_composition)
        re.save()
        return redirect('revised_composition')
    return render(request,'revised_composition.html')


def gst_stock_item(request):
    return render(request,'gst_stock_item.html')


def gst_stock(request):
    gst=gst_stockitem.objects.all()
    if request.method=='POST':
        calc_typ=request.POST['calc_typ']
        taxability=request.POST['taxability']
        g=gst_stockitem(taxability=taxability,calc_typ=calc_typ)
        g.save()
        return redirect('gst_stock')
    return render(request,'gst_stock_item.html')

def load_tds(request):
    return render(request,'tds_details.html')

def tds_d(request):
    tds=Tds_Details.objects.all()
    if request.method=='POST':
        tan_reg_no=request.POST['tan_reg_no']
        acc_no=request.POST['acc_no']
        d_typ=request.POST['d_typ']
        d_branch=request.POST['d_branch']
        set_alter=request.POST['set_alter']
        it_tds=request.POST['it_tds']
        act_tds=request.POST['act_tds']
        t=Tds_Details(tan_regno=tan_reg_no,tan=acc_no,deductor_type=d_typ,deductor_branch=d_branch,person_details=set_alter,ignore_it=it_tds,active_tds=act_tds)
        t.save()
        return redirect('tds_d')
    return render(request,'tds_details.html')

def load_person_res(request):
    return render(request,'person_res.html')

def person_res(request):
    person=tds_person.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        son=request.POST['son']
        designation=request.POST['designation']
        pan=request.POST['pan']
        flat_no=request.POST['flat_no']
        name_bul=request.POST['name_bul']
        road=request.POST['road']
        location=request.POST['location']
        city=request.POST['city']
        state=request.POST['state']
        pincode=request.POST['pincode']
        mob_no=request.POST['mob_no']
        std=request.POST['std']
        tele_phn=request.POST['tele_phn']
        email=request.POST['email']
        p=tds_person(name=name,son_daughter=son,designation=designation,pan=pan,flat_no=flat_no,building=name_bul,street=road,area=location,town=city,
        state=state,pincode=pincode,mobile=mob_no,std=std,telephone=tele_phn,email=email)
        p.save()
        return redirect('person_res')
    return render(request,'person_res.html')

def load_gst_d(request):
    return render(request,'gst_d.html')

def gst_d(request):
    gst=GST.objects.all()
    if request.method=='POST':
        state=request.POST['state']
        reg_typ=request.POST['reg_typ']
        assess_of_teritory=request.POST['assess_of_teritory']
        gst_application=request.POST['gst_application']
        uin=request.POST['uin']
        periodicity=request.POST['periodicity']
        flood_access=request.POST['flood_access']
        applicable_from=request.POST['applicable_from']
        set_alter=request.POST['set_alter']
        tax_liability_advance=request.POST['tax_liability_advance']
        tax_liability_reverse=request.POST['tax_liability_reverse']
        gst_clss=request.POST['gst_clss']
        lut_but=request.POST['lut_but']
        tax_cal=request.POST['tax_cal']
        tax_rate_turnover=request.POST['tax_rate_turnover']
        tax_rate_purchase=request.POST['tax_rate_purchase']
        e_way_bill=request.POST['e_way_bill']
        appl_from=request.POST['appl_from']
        th_limlit_in=request.POST['th_limlit_in']
        th_limit=request.POST['th_limit']
        appl_intrastate=request.POST['appl_intrastate']
        thr_limit=request.POST['thr_limit']
        p_e_way=request.POST['p_e_way']
        e_invoice=request.POST['e_invoice']
        appli_frm=request.POST['appli_frm']
        bill_from_place=request.POST['bill_from_place']
        period_report=request.POST['period_report']
        send_eway_bill=request.POST['send_eway_bill']
        g=GST(state=state,reg_type=reg_typ,assessee=assess_of_teritory,gst_applicable=gst_application,gstin=uin,periodicity=periodicity,flood_cess=flood_access,
        applicable_from=applicable_from,gst_rate_details=set_alter, advance_receipts= tax_liability_advance,reverse_charge=tax_liability_reverse,
        gst_classification=gst_clss,bond_details=lut_but,tax_calc=tax_cal,tax_rate=tax_rate_turnover,tax_purchase=tax_rate_purchase, eway_bill=e_way_bill,
        applicable_form=appl_from,threshold_includes=th_limlit_in,threshold_limit=th_limit,intrastate=appl_intrastate,threshold_limit2=thr_limit, print_eway= p_e_way,e_invoice=e_invoice,
        app_from=appli_frm,billfrom_place=bill_from_place,dperiod=period_report,send_ewaybill=send_eway_bill)
        g.save()
        return redirect('gst_d')
    return render(request,'gst_d.html')

def load_lut_bond(request):
    return render(request,'lut_bond A.html')

def lutbond(request):
    lut=gst_lutbond.objects.all()
    if request.method=='POST':
        lut_no=request.POST['lut_no']
        appl_from=request.POST['appl_frm']
        appl_to=request.POST['appl_to']
        l=gst_lutbond(lutbond=lut_no,validity_from=appl_from,validity_to=appl_to)
        l.save()
        return redirect('lutbond')
    return render(request,'lut_bond A.html')

def load_gst_details_c(request):
    return render(request,'gst_details_c.html')

def gst_details_c(request):
	gst=gst_taxability.objects.all()
	if request.method=='POST':
		taxability=request.POST['taxability']
		tax=request.POST['tax']
		cess=request.POST['cess']
		kerela_fc=request.POST['flood_cess']
		g=gst_taxability(taxability=taxability,integrated_tax=tax,cess=cess,flood_cess=kerela_fc)
		g.save()
		return redirect('gst_details_c')
	return render(request,'gst_details_c.html')