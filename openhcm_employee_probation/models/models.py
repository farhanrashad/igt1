# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from datetime import datetime
from dateutil import relativedelta
from openerp.tools.translate import _
from passlib import context


class HrEmployeeInh(models.Model):
    _inherit = 'hr.employee'

    status_employee = fields.Selection([
        ('probation', 'Probation'),
        ('employment', 'Employment'),
        ('noticePeriod', 'Notice Period'),
        ('resigned', 'Resigned'),
        ('terminated', 'Terminated'), ],
        string='Employee Status', default='probation')


class HrEmployeeProbation(models.Model):
    _name = 'employee.probation.period'
    _description = 'openhcm_employee_probation'

    # Gorup 1
    employee_id = fields.Many2one('hr.employee', string='Employee',
                                  ondelete='set null',
                                  index="True")
    line_manager = fields.Many2one(related='employee_id.parent_id', string='Line Manager',
                                   ondelete='set null',
                                   index="True")
    head_of_function = fields.Many2one(related='employee_id.parent_id', string='Head Of Function',
                                       ondelete='set null',
                                       index="True")
    progress_rate = fields.Selection([('star0', '<p class="star-rating"><a href="" data-star="1"><i class="fa '
                                                'fa-star"></i></a></p>'),
                                      ('start1', '<p class="star-rating"><a href="" data-star="1"><i class="fa '
                                                 'fa-star"></i></a></p>'),
                                      ('start2', '<p class="star-rating"><a href="" data-star="1"><i class="fa '
                                                 'fa-star"></i></a></p>'),
                                      ('start3', '<p class="star-rating"><a href="" data-star="1"><i class="fa '
                                                 'fa-star"></i></a></p>'),
                                      ('start4', '<p class="star-rating"><a href="" data-star="1"><i class="fa '
                                                 'fa-star"></i></a></p>'),
                                      ('start5', '<p class="star-rating"><a href="" data-star="1"><i class="fa '
                                                 'fa-star"></i></a></p>'),
                                      ('start6', '<p class="star-rating"><a href="" data-star="1"><i class="fa '
                                                 'fa-star"></i></a></p>')],
                                     select=True
                                     )

    # Group 2
    contract = fields.Char(related='employee_id.name', string='Contract',)
    department = fields.Many2one(related='employee_id.department_id', string='Department',
                                 ondelete='set null',
                                 index="True"
                                 )
    job_position = fields.Many2one(related='employee_id.job_id', string='Job Position',
                                   ondelete='set null',
                                   index="True")
    join_date = fields.Date(string='Join Date', required=True)
    probation_complete_date = fields.Date(string='Probation Complete Date', required=True)

    state = fields.Selection([('draft', 'Draft'),
                              ('waiting approval', 'Waiting Approval'),
                              ('done', 'Done'),
                              ('refuse', 'Refuse')
                              ],
                             string='Status', default='draft')
    plan_data = fields.Text(compute='set_greet_message')
    employment_status = fields.Char(string='Employment Status', compute='employee_status')
    get_review = fields.Text("review")
    current_date = fields.Date(default=date.today())
    check = fields.Boolean()
    current_user = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.uid)
    responsible_id = fields.Char(related='employee_id.work_email', string='Email',
                                 ondelete='set null',
                                 index="True")
    refuse_check = fields.Boolean(default=True)
    #print('outside',refuse_check)

    @api.depends('join_date', 'probation_complete_date')
    def set_greet_message(self):
        t = self.probation_complete_date
        r = relativedelta.relativedelta(t, self.join_date)
        if not self.plan_data:
            self.plan_data = "unknown"
        self.plan_data = (" {0} Months Probation Period  start from Date {1}".format(r.months, self.join_date))
        print("Moths of probation", r.months)

    @api.depends('probation_complete_date')
    def employee_status(self):
        print('probation_complete_date =', self.probation_complete_date)
        self.check = False
        self.employment_status = 'Probation'
        if self.probation_complete_date:
            print('probation_complete_date inside if =', self.probation_complete_date)
            print('1st if check=', self.check)
            if self.probation_complete_date <= date.today():
                self.employment_status = 'Employment'
                self.check = True
                emp = self.env['hr.employee'].search([('id', '=', self.employee_id.id)])
                emp.status_employee = 'employment'
                print('2nd if check=', self.check)
            else:
                emp = self.env['hr.employee'].search([('id', '=', self.employee_id.id)])
                emp.status_employee = 'probation'

    def set_probation_plan(self):
        self.state = 'waiting approval'
        template_id = self.env.ref('openhcm_employee_probation.email_template_employee_probation').id
        template = self.env['mail.template'].browse(template_id)
        self.env['mail.template'].browse(template_id).send_mail(self.id)
        print("template id : ", template_id)
        print("template is : ", template)
        print('set_probation_plan')
        # id=self.employee_id.id
        # self.env['hr.employee'].search([(id)])
        emp = self.env['hr.employee'].search([('id', '=', self.employee_id.id)])
        emp.status_employee = 'probation'

    def send_review(self):
        self.state = 'done'
        print('send_review')

    def refuse(self):
        print('refuse')
        self.state = 'refuse'
        self.refuse_check = False
        print('inside method',self.refuse_check)

    def action_review_wizard(self):
        wizard_view_id = self.env.ref(
            'openhcm_employee_probation.hr_recruitment_probation_period_form_wizard')
        xm = self.id
        print('active id', xm)
        return {
            'name': _('Add Review'),
            'res_model': 'employee.probation.wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'context': {'current_id': self.id},
            'view_id': wizard_view_id.id,
            'target': 'new',
        }
