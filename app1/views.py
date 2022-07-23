from django.shortcuts import render,redirect
from .models import tally_group

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
    return render(request, 'jisha/cost.html')

def rates(request):
    return render(request, 'jisha/rates.html')

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


def cn(request):
    return render(request, 'jisha/cn.html')

def add_group(request):
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
