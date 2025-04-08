# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Real Estate',
    'version' : '17.0.1.0.0',
    'summary': 'Real Estate',
    'author': 'Usama Wazir',
    'sequence': -99,
    'description': """Real Estate""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'license' : 'LGPL-3',
    'depends' : ['sale','mail' , 'product' , 'base'],
    'data': [
        # Security
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        # Views
        'views/estate_property_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_menus.xml',
        #
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb':[],
    'installable': True,
    'application': True,
    'auto_install':False,
}
