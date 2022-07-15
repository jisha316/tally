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

    path('cn',views.cn,name='cn'),
    
]