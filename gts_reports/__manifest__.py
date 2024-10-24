# -*- encoding: utf-8 -*-

{
    'name': 'CLSS Reports',
    'version': '17.0.0.0',
    'category': 'Integration',
    'summary': """""",

    'author': 'Geo Technosoft',
    'description': 'This module Allows you to generate Report',
    'sequence': 1,
    'website': 'https://www.geotechnosoft.com',
    'depends': ['base','account','base_vat','stock_sms'],
    'data': [
        # 'security/einvoice_user_groups.xml',
        # 'security/ir.model.access.csv',
        'reports/vat_invoice_arabic.xml',
        'views/arabic_address.xml',

    ],
    'images': ['static/description/banner.png'],
    'price': 99.00,
    'currency': 'USD',
    'license': 'OPL-1',
    'application': True,
    'installable': True,
}
