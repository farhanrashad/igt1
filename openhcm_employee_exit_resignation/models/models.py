# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime


class HrEmployeeExitResignation(models.Model):
    _name = 'hr.employee.exit.resignation'
    _description = 'This is Employee Exit'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    
    def unlink(self):
        for leave in self:
            if leave.state in ('confirm','approved_manager','approved_hr_manager','approved_general_manager','done'):
                raise UserError(_('You cannot delete an order form  which is not draft or close. '))
     
            return super(HrEmployeeExitResignation, self).unlink()
    


    name = fields.Char(string="Employee Name", required=True)
    request_Date = fields.Date(string='Request Date', default=datetime.today() , required=True)
    last_day_of_work = fields.Date(string='Last Day Of Work',required=True)
    contact = fields.Many2one('res.partner', ondelete='set null',
                              string="Contact", index="True", required=True)
    department_id = fields.Many2one('hr.department', 'Department',
                                    ondelete='set null',
                                    index="True"
                                    )
    job_id = fields.Many2one('hr.job', 'Job Position',
                             ondelete='set null',
                             index="True" , required=True)
    parent_id = fields.Many2one('hr.employee', 'Manager',
                                ondelete='set null',
                                index="True")

    user_id = fields.Many2one('hr.employee', 'User',
                              ondelete='set null',
                              index="True" , required=True)
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
    employ_information = fields.Many2many('hr.employee.exit.resignation.notebook', 'resignation_id', string='Information')

    reason_for_exit = fields.Char(string="Reason for exit")
    notes = fields.Text(string="Note")
    start_interview = fields.Char(string='Start Interview')
    print_Interview = fields.Char(string='Start Interview')
    meeting = fields.Char(string='Start Interview')
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ('approved_manager', 'Approved by Dept. Manager'),
                              ('approved_hr_manager', 'Approved by Hr Manager'),
                              ('approved_general_manager', 'Approved by General Manager'),
                              ('done', 'done')],
                             string='Status', default='draft')
    work_mobile = fields.Char(string='Mobile')
    work_email = fields.Char(string='Email')
    address = fields.Text(string='Address')

    def done_action(self):
        self.write ({
            'state' : 'done'
        })

    def action_browse(self):
        print("Current Record is : ")
        self.state = 'confirm'
        self.department_manager_approve_date = datetime.now()
        self.Confirm_by = self._uid

    @api.depends('Department_manager , department_manager_approve_date')
    def approved_by_dept_manager(self):
        print(" dept Manager :", self.Department_manager)
        self.state = 'approved_manager'
        self.department_manager_approve_date = datetime.now()
        self.Department_manager = self._uid

    @api.depends('Hr_manager,hr_manger_approved_date')
    def approved_by_hr_manager(self):
        print("hr Manager :", self.Hr_manager)
        self.state = 'approved_hr_manager'
        self.hr_manger_approved_date = datetime.now()
        self.Hr_manager = self._uid

    @api.depends('General_manager,general_manager_approved_date')
    def approve_by_general_manager(self):
        print("General Manager :", self.General_manager)
        self.state = 'approved_general_manager'
        self.general_manager_approved_date = datetime.now()
        self.General_manager = self._uid


class HrEmployeeExitResignationChecklist(models.Model):
    _name = 'hr.employee.exit.resignation.checklist'
    _description = 'Employee Checklist'
    
    def action_confirm(self):
        self.write ({
            'state' : 'confirm'
        })
        
    def action_approved(self):
        self.write ({
            'state' : 'approved'
        })
        
    def unlink(self):
        for leave in self:
            if leave.state in ('confirm','approved'):
                raise UserError(_('You cannot delete an order form  which is not draft or close. '))
     
            return super(HrEmployeeExitResignationChecklist, self).unlink()    
    

    resignation_id = fields.Many2one('hr.employee.exit.resignation', string='Information')
    name = fields.Many2one('hr.employee.exit.resignation.checklist', string="Checklist")
    User_id = fields.Many2one('res.users', string='Responsible User',
                                       ondelete='set null',
                                       index="True")
    Remarks = fields.Text(string="Remarks")
    checklist_lines = fields.One2many('hr.employee.exit.resignation.checklist.line', 'checklist_id' ,string="Checklist Line")
    state = fields.Selection([('new', 'New'),
                              ('confirm', 'Confirm'),
                              ('approved', 'Approved'),                            
                             string='Status', default='new')
                              
                              
class HrEmployeeExitResignationChecklistLine(models.Model):
    _name = 'hr.employee.exit.resignation.checklist.line'
    _description = 'Employee Checklist'
    
   
    checklist_id = fields.Many2one('hr.employee.exit.resignation.checklist', string='checklist') 
    name = fields.Char(string="Name")                          
