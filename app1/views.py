import datetime
from datetime import timedelta
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')


def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')

#......................jisha........................
def ledgers(request):
	grp=tally_group.objects.all()
	context={'grp' : grp}
	return render(request,'jisha/ledgers.html',context)

def ledg(request):
    return render(request, 'jisha/ledg.html')

def vouchers(request):
    return render(request, 'jisha/vouchers.html')

def groups(request):
    return render(request, 'jisha/groups.html')

def currency(request):
    return render(request, 'jisha/currency.html')

def c_create(request):
    return render(request, 'jisha/c_create.html')

def c_alter(request):
    return render(request, 'jisha/c_alter.html')

def cost(request):
	costt=cost_centre.objects.all()
	context={'costt' : costt}
	return render(request,'jisha/cost.html',context)

def rates(request):
	ccr=crt_currency.objects.all()
	context={'ccr' : ccr}
	return render(request,'jisha/rates.html',context)

def cmpny_list(request):
    return render(request, 'jisha/cmpny_list.html')

def create_cmpny(request):
    return render(request, 'jisha/create_cmpny.html')

def gst(request):
    return render(request, 'jisha/gst.html')

def gst_details(request):
    return render(request, 'jisha/gst_details.html')

def select_c(request):
	sel = create_company.objects.all()
	context={'sel' : sel}
	return render(request,'jisha/select_c.html',context)

def features(request):
	return render(request, 'jisha/features.html')

def tds(request):
    return render(request, 'jisha/tds.html')

def tds_details(request):
    return render(request, 'jisha/tds_details.html')

def c_rates(request):
    return render(request, 'jisha/c_rates.html')

def bank_details(request):
	return render(request,'jisha/bank_details.html')

def shut_cmpny(request):
    return render(request, 'jisha/shut_cmpny.html')

def shut_msg(request):
    return render(request, 'jisha/shut_msg.html')

def lut_bond(request):
    return render(request, 'jisha/lut_bond.html')

def cheque(request):
    return render(request, 'jisha/cheque.html')

def ledger_gst(request):
    return render(request, 'jisha/ledger_gst.html')

def ledger_chequed(request):
    return render(request, 'jisha/ledger_chequed.html')

def vouch_advance(request):
    return render(request, 'jisha/vouch_advance.html')

def gst_1(request):
    return render(request, 'jisha/gst_1.html')

def ledger_taxgst(request):
    return render(request, 'jisha/ledger_taxgst.html')


def cn(request):
    return render(request, 'jisha/cn.html')

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
		crny=crt_currency(c_symbol=smbl,
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

def create_ROE(request):
	if request.method=='POST':
		dt=request.POST['dt']
		crname=request.POST['curname']
		stdr=request.POST['stdr']
		ssr=request.POST['ssr']
		bsr=request.POST['bsr']
		croe=currency_ROE(date_ROE=dt,
                        currency_name = crname,
                        std_rate = stdr,
                        selling_SR = ssr,
                        buying_SR = bsr)          
		croe.save()
		return redirect('/')
	return render(request,'rates.html')

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
		crny=alt_currency(c_symbol=smbl,
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
	if request.method=='POST':
		nm=request.POST['cst_name']
		als=request.POST['alias']
		unr=request.POST['c_under']
		cost=cost_centre(centre_name=nm,
                        centre_alias = als,
                        centre_under = unr)          
		cost.save()
		print("added")
		return redirect('/')

def create_tds(request):
	if request.method=='POST':
		t_reg = request.POST['tan_reg_no']
		tax_clct = request.POST['tax_ded_clctn']
		ded_type = request.POST['deductor_type']
		ded_bd = request.POST['ded_brachdevision']
		prsn_res = request.POST['person_res']
		ignr = request.POST['ignore_it']
		st_itm = request.POST['tds_stock_items']
		
		ctds=tally_tds(tan_reg_no=t_reg,
                        tax_ded_clctn = tax_clct,
                        deductor_type = ded_type,
                        ded_brachdevision = ded_bd,
                        person_res = prsn_res,
                        ignore_it = ignr,
                        tds_stock_items = st_itm)          
		ctds.save()
		print("added")
		return redirect('/')
	return render(request,'jisha/tds.html')

def person_tds(request):
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
	    
		prs=person_res_details(name=name,
                        son_daughter = sd,
                        designation = des,
                        pan = pan,
                        flat_no = ftno,
                        premise_name = pnm,
                        street = str,
                        area = are,
                        city = city,
                        state = st,
                        pincode = pcd,
                        mobile_no = m_no,
                        std_code = std,
                        telephone = tph,
                        email = emal)          
		prs.save()
		print("added")
		return redirect('person_tds')
	return render(request,'jisha/tds_details.html')

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

		vhr=tally_vouchers(voucher_name=nm,
                    alias = als,
                    voucher_type = vtp,
                    Abbreviation = abbr,
                    activate_Vtype = actp,
                    method_Vno = mvno,
                    prevent = prnt,
                    advance_con = acn,
                    use_EDV = use,
                    zero_val = zero,
                    mVoptional_defualt = mvd,
                    allow_nar = anar,
                    provide_L = prvdl,
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

def create_gstdetails(request):
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
                        flood_cess = fc)          
		cost.save()
		print("Added")
		return redirect('gst_details')
	return render(request,'jisha/gst_details')

def create_lutbond(request):
	if request.method=='POST':
		lbno=request.POST['lut_bondNo']
		afrom=request.POST['application_from']
		ato=request.POST['application_to']
		# u=tally_gst.objects.get('')  
		lb=gst_lutbond(lut_bond_No=lbno,
                        validity_from = afrom,
                        validity_to = ato)      
		lb.save() 
		print("Added")
		return redirect('lut_bond')
	return render(request,'jisha/lut_bond')

def create_gst(request):
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
        
		gstd=tally_gst(state=st,
						registration_type=rt,
						assessee_territory=at,
						gst_applicable=gsta,
						gstin_uin=gstuin,
						periodicity=prd,
					# ........regular.......
						kerala_fca=kfca,
						applicable_from=af,
						gst_rate_details=gstrd,
						tl_advanceR=tla,
						tl_reverseC=tlr,
						gst_classification=gstc,
						lut_bond=lb,	
					# ........composition.......
						tax_rate=tr,		
						tax_calculation=tc,		
						tax_purchase=tp,
					# ........e-Way bill applicable.......
						e_waybillA=ea,
						applicable_f=aaf,
						thresholdlimit_include=tli,
						threshold_limit=tl,
						intrastate=intr,
						ithreshold_limit=itl,
						print_eway=pnw,
					# ........e-Invoice applicable.......
						e_invoiceA=einva,
						app_from=appf,
						billfrom_place=bfp,
						period_einvoiceR=peir,
						send_eW_details_einvoice=sewdei)
		gstd.save()
		print("Added")
		return redirect('/')
		

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
        return render(request,'jisha/ledgers.html')

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
	return render(request,'jisha/ledger_chequed.html')

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

		ccmp=create_company.objects.filter(company_name=name)
		out=datetime.datetime.strptime (fin_begin,'%Y-%m-%d')+timedelta (days=364) 
		a=out.date()
		

		if ccmp:
			messages.info(request,'Company name already exists!!')
			return redirect('create_cmpny')
		else:
			cmp=create_company(company_name=name,mailing_name=mname,address=addr,state=st,country=cntry,
                pincode=pncd,telephone=tlphn,mobile_no=mbl,fax=fax,email=email,website=wbsit,fin_begin=fin_begin,
                books_begin=bk_begin,currency_symbol=crny_symbol,formal_name=frml_name,fin_end=a)
			cmp.save()
			messages.info(request,'Company created successfully(Enable the features as per your business needs)')
			return render(request,'jisha/features.html',{'cmp':cmp})

def company_feature(request,cf):
	id=create_company.objects.get(id=cf)
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

		cmp_fet=company_features(maintain_account=ma,billwise_entry=be,cost_centre=cc,interest_calculation=ic,maintain_inventry=mi,
		account_inventry=ai,multiple_pricelevel=mpl,enable_batches=eb,expiry_date=edt,job_order_procress=jop,cost_tracking=ct,job_costing=jc,discount_column=dc,
		seperte_actual=sa,gst=gst,tds=tds,tcs=tcs,vat=vat,excise=excise,service_tax=st,payroll=prl,multiple_address=maddr,
		mark_modified=mark_mod,company=id)

		cmp_fet.save()
		return redirect('/')
	return render(request,'jisha/features.html',{'cmp':id})

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
                        bank_name =bank_name )      
		lbd.save() 
		print("Added")
		return redirect('bank_details')
	return render(request,'jisha/bank_details.html')

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
	return render(request,'jisha/cheque.html')

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
	return render(request,'jisha/ledger_gst.html')

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
	return render(request,'jisha/vouch_advance.html')

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
	return render(request,'jisha/ledger_taxgst.html')

