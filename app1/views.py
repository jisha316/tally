from django.shortcuts import render,redirect
from .models import *
# from .models import tally_group,tally_currency,alt_currency,cost_centre,tally_tds,person_res_details,tally_vouchers,gst_lutbond,gst_taxability,currency_ROE

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
    return render(request, 'jisha/ledgers.html')

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
	cr=currency_ROE.objects.all()
	return render(request,'jisha/rates.html',{'cr' : cr})

def cmpny_list(request):
    return render(request, 'jisha/cmpny_list.html')

def create_cmpny(request):
    return render(request, 'jisha/create_cmpny.html')

def gst(request):
    return render(request, 'jisha/gst.html')

def gst_details(request):
    return render(request, 'jisha/gst_details.html')

def select_c(request):
    return render(request, 'jisha/select_c.html')

def features(request):
    return render(request, 'jisha/features.html')

def tds(request):
    return render(request, 'jisha/tds.html')

def tds_details(request):
    return render(request, 'jisha/tds_details.html')

def c_rates(request):
    return render(request, 'jisha/c_rates.html')

def bank_details(request):
    return render(request, 'jisha/bank_details.html')

def shut_cmpny(request):
    return render(request, 'jisha/shut_cmpny.html')

def shut_msg(request):
    return render(request, 'jisha/shut_msg.html')

def lut_bond(request):
    return render(request, 'jisha/lut_bond.html')

def gst_1(request):
    return render(request, 'jisha/gst_1.html')


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
		crny=tally_currency(c_symbol=smbl,
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
		return redirect('/')

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
		return redirect('/')

def create_lutbond(request):
	if request.method=='POST':
		lbno=request.POST['lut_bondNo']
		afrom=request.POST['application_from']
		ato=request.POST['application_to']
		lb=gst_lutbond(lut_bond_No=lbno,
                        validity_from = afrom,
                        validity_to = ato)          
		lb.save()
		print("Added")
		return redirect('/')

def create_ROE(request):
	if request.method=='POST':
		dt=request.POST['dt']
		crncy=request.POST['curname']
		cr=tally_currency.objects.get(id=crncy)
		stdr=request.POST['stdr']
		ssr=request.POST['ssr']
		bsr=request.POST['bsr']
		croe=currency_ROE(date_ROE=dt,
                        currency = cr,
                        std_rate = stdr,
                        selling_SR = ssr,
                        buying_SR = bsr)          
		croe.save()
		print("Added")
		return redirect('/')
	
def create_gst(request):
    if request.method=='POST':
        state = request.POST['state']
        rt = request.POST['registration_type']
        at = request.POST['assessee_territory']
        gsta = request.POST['gst_applicable']
        gstuin = request.POST['gstin_uin']
        prd = request.POST['periodicity']
        kfca = request.POST['kerala_fca']
        af = request.POST['applicable_from']
        gstrd = request.POST['gst_rate_details']
        tla = request.POST['tl_advanceR']
        tlr = request.POST['tl_reverseC']
        gstc = request.POST['gst_classification']
        lb = request.POST['lut_bond']
        tr = request.POST['tax_rate']
        tc = request.POST['tax_calculation']
        tp = request.POST['tax_purchase']

        eA = request.POST('e_waybillA')
        aaf = request.POST['applicable_f']
        tli = request.POST['thresholdlimit_include']
        tl = request.POST['threshold_limit']
        intr = request.POST['intrastate']
        itl = request.POST['ithreshold_limit']
        pnw = request.POST['print_eway']

        einva = request.POST['e_invoiceA']
        appf = request.POST['app_f']
        bfp = request.POST['billfrom_place']
        peir = request.POST['period_einvoiceR']
        sewdei = request.POST['send_eW_details_einvoice']
        gstd=gst_details(state=state,
						registration_type=rt,
						assessee_territory=at,
						gst_applicable=gsta,
						gstin_uin=gstuin,
						periodicity=prd,
						kerala_fca=kfca,
						applicable_from=af,
						gst_rate_details=gstrd,
						tl_advanceR=tla,
						tl_reverseC=tlr,
						gst_classification=gstc,
						lut_bond=lb,		
						tax_rate=tr,		
						tax_calculation=tc,		
						tax_purchase=tp,
						e_waybillA=eA,
						applicable_f=aaf,
						thresholdlimit_include=tli,
						threshold_limit=tl,
						intrastate=intr,
						ithreshold_limit=itl,
						print_eway=pnw,

						e_invoiceA=einva,
						app_from=appf,
						billfrom_place=bfp,
						period_einvoiceR=peir,
						send_eW_details_einvoice=sewdei)
		gstd
		