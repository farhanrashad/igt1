# -*- coding: utf-8 -*-
{
    'name': 'Employee Vehicle Request',
    'version': '12.0.1.0.0',
    'summary': """Manage Vehicle Requests From Employee""",
    'description': """This module is used for manage vehicle requests from employee.
                   This module also checking the vehicle availability at the requested time slot.""",
    'category': "Generic Modules/Human Resources",
    'author': 'Obaid',
    'company': 'Dynexcel',
    'website': "https://http://www.dynexcel.co",
    'depends': ['base', 'hr', 'fleet'],
    'data': [
        'data/data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/employee_fleet_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
