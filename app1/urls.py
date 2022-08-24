from django.urls import path
from.import views


urlpatterns = [

    path('',views.base,name='base'),

#.........................jisha..........................   

    path('ledgers',views.ledgers,name='ledgers'),

    path('vouchers',views.vouchers,name='vouchers'),

    path('groups',views.groups,name='groups'),

    path('group_alt',views.group_alt,name='group_alt'),

    path('cost_alt',views.cost_alt,name='cost_alt'),

    path('currency',views.currency,name='currency'),

    path('c_create',views.c_create,name='c_create'),

    path('c_alter',views.c_alter,name='c_alter'),

    path('cost',views.cost,name='cost'),
    
    path('rates',views.rates,name='rates'),

    path('change_company',views.change_company,name='change_company'),

    path('company_list',views.company_list,name='company_list'),

    path('select_c',views.select_c,name='select_c'),

    path('create_cmpny',views.create_cmpny,name='create_cmpny'),
    
    path('features',views.features,name='features'),

    path('tally_gst/<int:pk>',views.tally_gst,name='tally_gst'),

    path('create_gst/<int:pk>',views.create_gst,name='create_gst'),

    path('gst_tax/<int:pk>',views.gst_tax,name='gst_tax'),

    path('lut_bond',views.lut_bond,name='lut_bond'),

    path('create_gsttax/<int:pk>',views.create_gsttax,name='create_gsttax'),

    path('create_lutbond',views.create_lutbond,name='create_lutbond'),

    path('tds/<int:pk>',views.tds,name='tds'),

    path('create_tds/<int:pk>',views.create_tds,name='create_tds'),

    path('person_tds/<int:pk>',views.person_tds,name='person_tds'),

    path('person/<int:pk>',views.person,name='person'),

    path('bank_details',views.bank_details,name='bank_details'),

    path('bankname',views.bankname,name='bankname'),

    path('shut_cmpny',views.shut_cmpny,name='shut_cmpny'),

    path('shut/<int:pk>',views.shut,name='shut'),

    path('enable/<int:pk>',views.enable,name='enable'),

    path('b_name',views.b_name,name='b_name'),

    path('cheque',views.cheque,name='cheque'),

    path('ledger_gst',views.ledger_gst,name='ledger_gst'),

    path('vouch_advance',views.vouch_advance,name='vouch_advance'),

    path('ledger_chequed',views.ledger_chequed,name='ledger_chequed'),

    path('create_group',views.create_group,name='create_group'),

    path('create_currency',views.create_currency,name='create_currency'),

    path('alter_currency',views.alter_currency,name='alter_currency'),

    path('load_centre',views.load_centre,name='load_centre'),

    path('ledger_taxgst',views.ledger_taxgst,name='ledger_taxgst'),

    path('create_voucher',views.create_voucher,name='create_voucher'),

    path('create_ROE',views.create_ROE,name='create_ROE'),

    path('create_ledger',views.create_ledger,name='create_ledger'),

    path('create_ledgerdimension',views.create_ledgerdimension,name='create_ledgerdimension'),

    path('company_create',views.company_create,name='company_create'),

    path('company_feature/<int:cf>',views.company_feature,name='company_feature'),

    path('create_bankdetails',views.create_bankdetails,name='create_bankdetails'),

    path('create_chequebk',views.create_chequebk,name='create_chequebk'),

    path('create_ledger_gst',views.create_ledger_gst,name='create_ledger_gst'),

    path('create_voucher_advance',views.create_voucher_advance,name='create_voucher_advance'),

    path('create_ledger_taxgst',views.create_ledger_taxgst,name='create_ledger_taxgst'),
    
]