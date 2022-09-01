from django.urls import path
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('demo',views.demo,name='demo'),

#...........................................................

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
    
#======================================= Aswathy Work (app urls) ========================================
    path('godown_alt',views.godown_alt,name='godown_alt'),

    path('stockgroup_alt',views.stockgroup_alt,name='stockgroup_alt'),

    path('stockcate_alt',views.stockcate_alt,name='stockcate_alt'),

    path('unitcreate_alt',views.unitcreate_alt,name='unitcreate_alt'),

    path('new_uqcs',views.new_uqcs,name='new_uqcs'),

    path('load_stock_group',views.load_stock_group,name='load_stock_group'),
    path('stock_group',views.stock_group,name='stock_group'),
    path('load_stock_catagory',views.load_stock_catagory,name='load_stock_catagory'),
    path('stock_catagory',views.stock_catagory,name='stock_catagory'),
    path('load_unit_creation',views.load_unit_creation,name='load_unit_creation'),
    path('unit_sim',views.unit_sim,name='unit_sim'),
    path('load_unit_compound',views.load_unit_compound,name='load_unit_compound'),
    path('unit_com',views.unit_com,name='unit_com'),
    
    path('load_stock_item_creation',views.load_stock_item_creation,name='load_stock_item_creation'),
    path('stock_items',views.stock_items,name='stock_items'),
    path('load_company_price',views.load_company_price,name='load_company_price'),
    path('price_levels',views.price_levels,name='price_levels'),

    path('load_pan_cin',views.load_pan_cin,name='load_pan_cin'),
    path('pan_cin',views.pan_cin,name='pan_cin'),
    path('godown_creation',views.godown_creation,name='godown_creation'),
    path('godown',views.godown,name='godown'),

    path('load_rev',views.load_rev,name='load_rev'),
    path('revised',views.revised,name='revised'),
    path('load_rev_c',views.load_rev_c,name='load_rev_c'),
    path('revised_composition',views.revised_composition,name='revised_composition'),
    path('gst_stock_item',views.gst_stock_item,name='gst_stock_item'),
    path('gst_stock',views.gst_stock,name='gst_stock'),

    path('load_gst_d',views.load_gst_d,name='load_gst_d'),
    path('gst_d',views.gst_d,name='gst_d'),
    path('load_lut_bond',views.load_lut_bond,name='load_lut_bond'),
    path('lutbond',views.lutbond,name='lutbond'),
    path('load_gst_details_c',views.load_gst_details_c,name='load_gst_details_c'),
    path('gst_details_c',views.gst_details_c,name='gst_details_c'),

    path('load_tds',views.load_tds,name='load_tds'),
    path('tds_d',views.tds_d,name='tds_d'),
    path('load_person_res',views.load_person_res,name='load_person_res'),
    path('person_res',views.person_res,name='person_res'),
]

