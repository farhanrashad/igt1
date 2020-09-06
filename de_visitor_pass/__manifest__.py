# -*- coding: utf-8 -*-
{
    'name': "de_visitor_pass",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "By Dynexcel",
    'website': "http://www.dynexcel.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    "sequence": 7,
    # any module necessary for this one to work correctly
    'depends': ['hr'],

    # always loaded
    'data': [
        'security/visitor_security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/visitor_visit_duration_view.xml',
        'views/visitor_visit_category_view.xml',
        'views/visitor_visit_detail_view.xml',
        'reports/visitor_report_view.xml',
        'views/visitor_menu.xml',
        'reports/visitor_pass.xml',
        'reports/report.xml',






    ],
    # only loaded in demonstration mode

}
