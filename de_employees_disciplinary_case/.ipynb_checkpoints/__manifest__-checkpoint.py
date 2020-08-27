# -*- coding: utf-8 -*-
{
    'name': "de_employee_disciplinary_case",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dynexcel || Rai Muhammad Kashif",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','mail','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/offence.xml',
        'views/notice.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
