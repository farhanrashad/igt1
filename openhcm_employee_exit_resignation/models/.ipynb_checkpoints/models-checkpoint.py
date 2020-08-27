# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class HrEmployeeExitResignation(models.Model):
    _name = 'hr.employee.exit.resignation'
    _description = 'openhcm_employee_exit_resignation'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Employee Name")
    request_Date = fields.Date(string='Request Date', default=datetime.today())
    last_day_of_work = fields.Date(string='Last Day Of Work',required=True)
    contact = fields.Many2one('res.partner', ondelete='set null',
                              string="Contact", index="True")
    department_id = fields.Many2one('hr.department', 'Department',
                                    ondelete='set null',
                                    index="True"
                                    )
    job_id = fields.Many2one('hr.job', 'Job Position',
                             ondelete='set null',
                             index="True")
    parent_id = fields.Many2one('hr.employee', 'Manager',
                                ondelete='set null',
                                index="True")

    user_id = fields.Many2one('hr.employee', 'User',
                              ondelete='set null',
                              index="True")
    interview_id = fields.Char(string='Recruitment Form')
    Confirm_by = fields.Many2one('hr.employee', string='Confirmed By',
                                 ondelete='set null',
                                 readonly='True',
                                 index="True")
    Department_manager = fields.Many2one('hr.employee', string='Approved By Department Manager', readonly='True',
                                         ondelete='set null',
                                         index="True")
    Hr_manager = fields.Many2one('hr.employee', string='Approved By Hr Manager',readonly='True',
                                 ondelete='set null',
                                 index="True")
    General_manager = fields.Many2one('hr.employee', string='Approved By General Manager',readonly='True',
                                      ondelete='set null',
                                      index="True")
    confirm_date = fields.Date(string='Confirm Date(Employee)', default=datetime.today(), readonly='True')
    department_manager_approve_date = fields.Date(string='Approved Date', readonly='True')
    hr_manger_approved_date = fields.Date(string='Approved Date', readonly='True')
    general_manager_approved_date = fields.Date(string='Approved Date', readonly='True')
    employ_information = fields.One2many('hr.employee.exit.resignation.notebook', 'Information', string='Information')

    reason_for_exit = fields.Char(string="Reason for exit")
    notes = fields.Text(string="Note")
    start_interview = fields.Char(string='Start Interview')
    print_Interview = fields.Char(string='Start Interview')
    meeting = fields.Char(string='Start Interview')
    state = fields.Selection([('draft', 'Draft'),
                              ('Confirm', 'Confirm'),
                              ('Approved by Dept. Manager', 'Approved by Dept. Manager'),
                              ('Approved by Hr Manager', 'Approved by Hr Manager'),
                              ('Approved by General Manager', 'Approved by General Manager'),
                              ('cancel', 'cancel')],
                             string='Status', default='draft')

    def cancel_action(self):
        self.state = 'cancel'
        print("Cancel")

    def action_browse(self):
        print("Current Record is : ")
        self.state = 'Confirm'
        self.department_manager_approve_date = datetime.now()
        self.Confirm_by = self._uid

    @api.depends('Department_manager , department_manager_approve_date')
    def approved_by_dept_manager(self):
        print(" dept Manager :", self.Department_manager)
        self.state = 'Approved by Dept. Manager'
        self.department_manager_approve_date = datetime.now()
        self.Department_manager = self._uid

    @api.depends('Hr_manager,hr_manger_approved_date')
    def approved_by_hr_manager(self):
        print("hr Manager :", self.Hr_manager)
        self.state = 'Approved by Hr Manager'
        self.hr_manger_approved_date = datetime.now()
        self.Hr_manager = self._uid

    @api.depends('General_manager,general_manager_approved_date')
    def approve_by_general_manager(self):
        print("General Manager :", self.General_manager)
        self.state = 'Approved by General Manager'
        self.general_manager_approved_date = datetime.now()
        self.General_manager = self._uid


class HrEmployeeExitResignationNotebook(models.Model):
    _name = 'hr.employee.exit.resignation.notebook'
    _description = 'openhcm_employee_exit_resignation notebook'

    Information = fields.Many2one('hr.employee.exit.resignation', string='Information')
    Check_list = fields.Char(string="Checklist")
    Responsible_User = fields.Many2one('hr.employee', string='Responsible User',
                                       ondelete='set null',
                                       index="True")
    Remarks = fields.Text(string="Remarks")
    State = fields.Char(string="State")
