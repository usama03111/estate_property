# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
<<<<<<< HEAD
    'name': 'Real Estate',
    'version': '17.0.1.0.0',
=======
    'name' : 'Real Estate',
    'version' : '17.0.1.0.0',
>>>>>>> 05b39e2e21064740b2093465314b30c8cdd717a6
    'summary': 'Real Estate',
    'author': 'Usama Wazir',
    'sequence': -99,
    'description': """Real Estate""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
<<<<<<< HEAD
    'license': 'LGPL-3',
    'depends': ['sale', 'mail', 'product', 'base','website','portal','hr_recruitment'],
    'data': [

        # Security
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        # Data
        "data/estate.property.type.csv",
        "data/estate.property.offer.csv",
        "data/estate.property.tag.csv",
        "data/estate_property.xml",
        "data/estate.property.csv",

        # Views
        'wizard/report_wizard.xml',
        'views/estate_property_view.xml',
        'views/estate_property_type_view.xml',
        'views/estate_property_tag_view.xml',
        'views/estate_property_templete.xml',
        # 'views/real_estate_property_templete.xml',
        'views/estate_menus.xml',
        'views/website_menu.xml',
        "report/report_action.xml",
        "report/property_report_templete.xml",
        # Data

    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
=======
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
>>>>>>> 05b39e2e21064740b2093465314b30c8cdd717a6
}
