from django.shortcuts import render

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


def cn(request):
    return render(request, 'jisha/cn.html')
