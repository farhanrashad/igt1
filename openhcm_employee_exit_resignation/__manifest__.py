# -*- coding: utf-8 -*-
{
    'name': "openhcm_employee_exit_resignation",

    'summary': """ application for exit process of employ""",

    'description': """
        this module is for the process of the resignation of employ and his/her safe leave from the company
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'HR support',
    'version': '13.0.1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase','hr',],

    # always loaded
    'data': [
        'security/employee_exit_resignation_security.xml',
        'security/ir.model.access.csv',
        'views/employ_exit_resignation_view.xml',
        'views/employ_exit_resignation_menu.xml',
        'report/employee_report.xml',
        'report/report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'auto_install': False,
}
