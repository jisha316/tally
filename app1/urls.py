from django.urls import path
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),

#.........................jisha..........................
    path('ledgers',views.ledgers,name='ledgers'),

    path('vouchers',views.vouchers,name='vouchers'),

    path('groups',views.groups,name='groups'),

    path('currency',views.currency,name='currency'),

    path('c_create',views.c_create,name='c_create'),

    path('c_alter',views.c_alter,name='c_alter'),

    path('cost',views.cost,name='cost'),
    
    path('rates',views.rates,name='rates'),

    path('cmpny_list',views.cmpny_list,name='cmpny_list'),

    path('create_cmpny',views.create_cmpny,name='create_cmpny'),

    path('gst',views.gst,name='gst'),

    path('select_c',views.select_c,name='select_c'),
    
    path('features',views.features,name='features'),

    path('gst_details',views.gst_details,name='gst_details'),

    path('tds',views.tds,name='tds'),

    path('tds_details',views.tds_details,name='tds_details'),

    path('bank_details',views.bank_details,name='bank_details'),

    path('shut_cmpny',views.shut_cmpny,name='shut_cmpny'),

    path('shut_msg',views.shut_msg,name='shut_msg'),

    path('c_rates',views.c_rates,name='c_rates'),

    path('lut_bond',views.lut_bond,name='lut_bond'),

    path('cn',views.cn,name='cn'),

    path('gst_1',views.gst_1,name='gst_1'),

    path('cheque',views.cheque,name='cheque'),

    path('ledger_gst',views.ledger_gst,name='ledger_gst'),

    path('vouch_advance',views.vouch_advance,name='vouch_advance'),

    path('ledger_chequed',views.ledger_chequed,name='ledger_chequed'),

    path('create_group',views.create_group,name='create_group'),

    path('create_currency',views.create_currency,name='create_currency'),

    path('alter_currency',views.alter_currency,name='alter_currency'),

    path('load_centre',views.load_centre,name='load_centre'),

    path('create_tds',views.create_tds,name='create_tds'),

    path('person_tds',views.person_tds,name='person_tds'),

    path('create_voucher',views.create_voucher,name='create_voucher'),

    path('create_gstdetails',views.create_gstdetails,name='create_gstdetails'),

    path('create_lutbond',views.create_lutbond,name='create_lutbond'),

    path('create_ROE',views.create_ROE,name='create_ROE'),

    path('create_gst',views.create_gst,name='create_gst'),

    path('create_ledger',views.create_ledger,name='create_ledger'),

    path('create_ledgerdimension/<int:lc>',views.create_ledgerdimension,name='create_ledgerdimension'),

    path('company_create',views.company_create,name='company_create'),

    path('company_feature/<int:cf>',views.company_feature,name='company_feature'),

    
]