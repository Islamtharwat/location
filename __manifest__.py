# -*- coding: utf-8 -*-
{
    'name': "location",

    'summary': """
        Check in Meeting Location""",

    'description': """
        Employee make a Check In/Check Out Meeting Location to get the current location
    """,

    'author': "Eslam Tharwat",
    'license': 'AGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_attendance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_config.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
