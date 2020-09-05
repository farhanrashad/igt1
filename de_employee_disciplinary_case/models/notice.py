# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
import datetime


class HrEmployeeNotice(models.Model):
    _name = 'hr.employee.notice'
    _rec_name = 'name'
    _description = 'Hr Employee Offence'

    # notice_name = fields.Char("Name",)
    employee_id = fields.Many2one('hr.employee', 'Employee',required=True)
    parent_id = fields.Many2one('hr.employee', 'Manager',readonly=True)
    department_id = fields.Many2one('hr.employee', 'Department',readonly=True)
    user_id = fields.Many2one('res.user', 'User')
    job_title = fields.Many2one("hr.employee",string="Job Title",readonly=True)
    identity = fields.Many2one("hr.employee","Identification No",readonly=True)
    office_type = fields.Many2one("hr.employee.offence", required=True)
    warning_type = fields.Char("Warning Type", required=False)
    date = fields.Date(string='Creation Date', required=False)
    created_id = fields.Many2one("res.users",string='Created By')
    decision = fields.Text(string='Decision Of Interaction',required=True)
    improvement = fields.Text(string='Action Improvement',required=True)
    consequence = fields.Text(string='Consequence Future Interaction',required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done')
    ], readonly=True, index=True, copy=False, default='draft')

    name=fields.Char(string="Notice Sequence",required=True,copy=False,readonly=True,index=True,default=lambda self: _('New'))

    @api.model
    def create(self,vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('employee.notice') or _('New')
        result = super(HrEmployeeNotice, self).create(vals)
        return result

    def set_confirm(self):
        self.state="confirm"
        self.date=datetime.datetime.today()
        print(self.env.user.name,type(self.env.user))
        self.created_id=self.env.user

    def set_done(self):
        print("called-----")
        self.state='done'



