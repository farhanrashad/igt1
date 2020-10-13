# -- coding: utf-8 --
import datetime
from odoo import api, fields, models, _
from odoo.tools import float_compare
from odoo.exceptions import UserError, ValidationError, Warning

class HRApplicantINH(models.Model):
    _inherit = 'hr.applicant'

    pass



class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    # foreign key concept

    document_lines = fields.One2many('hr.employee.document', 'document_id', string='Employee education line',

                                  copy=True, auto_join=True)

    attachment_lines = fields.One2many('hr.employee.attachment', 'attachment_id', string='Employee education line',

                                  copy=True, auto_join=True)

    # family_lines = fields.One2many('hr.employee.family', 'family_id', string='Employee family line')


    # contact_lines = fields.One2many('hr.employee.contact.detail', 'contact_id', string='Employee contact line')


    dependents_lines = fields.One2many('hr.employee.dependent', 'dependent_id', string='Employee dependent line')



# language select option
language_fluency_choices = (
    ('Native','Native'),
    ('Basic', 'Basic'),
    ('Fluent','Fluent'),
)


class HrEmployeeDocument(models.Model):
    _name = 'hr.employee.document'
    _description = 'Employee Document'

    document_id = fields.Many2one('hr.employee', string='education_id',index=True, required=True,
                                          ondelete='cascade')
    doc_type = fields.Char(string='Document Type', store=True, required=True)
    doc_number = fields.Char(string='Number', store=True, required=True)
    issue_date = fields.Date(string='Issue Date', store=True, required=True)
    expiry_date = fields.Date(string='Expiry Date', store=True, required=True)


class HrEmployeeAttachment(models.Model):
    _name = 'hr.employee.attachment'
    _description = 'Employee attachment'
    attachment_id = fields.Many2one('hr.employee', string='attachment_id',index=True, required=True,
                                          ondelete='cascade')
    attachment = fields.Binary(string="Attach File", attachment=True)

# class HrEmployeeFamily(models.Model):
#     _name = 'hr.employee.family'
#     _description = 'Employee family'
#     family_id = fields.Many2one('hr.employee', string='family_id',index=True, required=True,
#                                           ondelete='cascade')
#     family_Owner = fields.Char(string='Owner Name', store=True, required=True)
#     Totalmember = fields.Char(string='total Member', store=True, required=True)


class HrEmployeeDependent(models.Model):
    _name = 'hr.employee.dependent'
    _description = 'Employee Dependent'
    dependent_id = fields.Many2one('hr.employee', string='Dependent Id',index=True, required=True,
                                          ondelete='cascade')
    name = fields.Char(string='Name', store=True, required=True)
    date_Of_birth = fields.Date(string='DOB', store=True, required=True)
    relationship = fields.Selection([('parent', 'Parent'),
                              ('gparent', 'Grand Parent'),
                              ('sib', 'Sibling'),
                              ('husb', 'Husband'),
                              ("wife", "Wife")],
                             default='parent')

