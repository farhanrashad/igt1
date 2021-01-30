
{
    'name': "Employee Orientation & Training",
    'version': '13.0.1.0.0',
    'category': "Generic Modules/Human Resources",
    'summary': """Employee Orientation/Training Program""",
    'description':'Complete Employee Orientation/Training Program',
    'author': 'Dynexcel',
    'company': 'Dynexcel',
    'website': 'https://www.dynexcel.co',
    'depends': ['base', 'hr'],
    'data': [
        'views/orientation_checklist_line.xml',
        'views/employee_orientation.xml',
        'views/orientation_checklist.xml',
        'views/orientation_checklists_request.xml',
        'views/orientation_checklist_sequence.xml',
        'views/orientation_request_mail_template.xml',
        'views/print_pack_certificates_template.xml',
        'views/report.xml',
        'views/employee_training.xml',
        'views/employee_training_sequence.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
