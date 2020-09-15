# -*- coding: utf-8 -*-
{
    'name': "openhcm_employee_probation",

    'summary': """
        This model is for record of probation of new employees""",

    'description': """
        Long description of module's purposeThis module keep record of new employees probation record. Joining date 
        to probation end date.
    """,

    'author': "Dynexcel",
    'website': "http://www.dynexcel.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hr Managment',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr','hr_recruitment','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/review_wizard1.xml',
        'views/openhcm_employee_probation_view.xml',
        'views/openhcm_employee_probation_menu.xml',
        'views/mail_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
