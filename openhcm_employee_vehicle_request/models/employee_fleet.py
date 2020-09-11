# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import Warning


class FleetReservedTime(models.Model):
    _name = "employee.fleet.reserved"
    _description = "Reserved Time"

    employee = fields.Many2one('hr.employee', string='Employee')
    date_from = fields.Datetime(string='Reserved Date From')
    date_to = fields.Datetime(string='Reserved Date To')
    reserved_obj = fields.Many2one('fleet.vehicle')


class FleetVehicleInherit(models.Model):
    _inherit = 'fleet.vehicle'
    _name = 'fleet.vehicle'
    

    check_availability = fields.Boolean(default=True, copy=False)
    reserved_time = fields.One2many('employee.fleet.reserved', 'reserved_obj', String='Reserved Time', readonly=1,
                                    ondelete='cascade')

    vehical_req_count = fields.Integer(compute="_compute_request_count_all")
 
    def _compute_request_count_all(self):
        for record in self:
            record.vehical_req_count = self.env['employee.fleet'].search_count([('fleet', '=', record.id)])



class EmployeeFleet(models.Model):
    _name = 'employee.fleet'
    _description = 'Employee Vehicle Request'
    _inherit = 'mail.thread'

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('employee.fleet')
        vals['req_date'] = datetime.today()
        return super(EmployeeFleet, self).create(vals)

    # @api.multi
    def send(self):
        if self.date_from and self.date_to:
            fleet_obj = self.env['fleet.vehicle'].search([])
            check_availability = 0
            for i in fleet_obj:
                for each in i.reserved_time:
                    if each.date_from <= self.date_from <= each.date_to:
                        check_availability = 1
                    elif self.date_from < each.date_from:
                        if each.date_from <= self.date_to <= each.date_to:
                            check_availability = 1
                        elif self.date_to > each.date_to:
                            check_availability = 1
                        else:
                            check_availability = 0
                    else:
                        check_availability = 0
            if check_availability == 0:
                reserved_id = self.fleet.reserved_time.create({'employee': self.employee.id,
                                                               'date_from': self.date_from,
                                                               'date_to': self.date_to,
                                                               'reserved_obj': self.fleet.id,
                                                               })
                self.write({'reserved_fleet_id': reserved_id.id})
                self.state = 'waiting'
            else:
                raise Warning('Sorry This vehicle is already requested by another employee')

    # @api.multi
    def approve(self):
        self.fleet.fleet_status = True
        self.state = 'confirm'
        mail_content = _('Hi %s,<br>Your vehicle request for the reference %s is approved.') % \
                       (self.employee.name, self.name)
        main_content = {
            'subject': _('%s: Approved') % self.name,
            'author_id': self.env.user.partner_id.id,
            'body_html': mail_content,
            'email_to': self.employee.work_email,
        }
        mail_id = self.env['mail.mail'].create(main_content)
        mail_id.mail_message_id.body = mail_content
        mail_id.send()
        if self.employee.user_id:
            mail_id.mail_message_id.write({'needaction_partner_ids': [(4, self.employee.user_id.partner_id.id)]})
            mail_id.mail_message_id.write({'partner_ids': [(4, self.employee.user_id.partner_id.id)]})

    # @api.multi
    def reject(self):
        self.reserved_fleet_id.unlink()
        self.state = 'reject'
        mail_content = _('Hi %s,<br>Sorry, Your vehicle request for the reference %s is Rejected.') % \
                       (self.employee.name, self.name)

        main_content = {
            'subject': _('%s: Approved') % self.name,
            'author_id': self.env.user.partner_id.id,
            'body_html': mail_content,
            'email_to': self.employee.work_email,
        }
        mail_id = self.env['mail.mail'].create(main_content)
        mail_id.mail_message_id.body = mail_content
        mail_id.send()
        if self.employee.user_id:
            mail_id.mail_message_id.write({'needaction_partner_ids': [(4, self.employee.user_id.partner_id.id)]})
            mail_id.mail_message_id.write({'partner_ids': [(4, self.employee.user_id.partner_id.id)]})

    # @api.multi
    def cancel(self):
        if self.reserved_fleet_id:
            self.reserved_fleet_id.unlink()
        self.state = 'cancel'

    # @api.multi
    def returned(self):
        self.reserved_fleet_id.unlink()
        self.returned_date = fields.datetime.now()
        self.state = 'return'

    @api.constrains('date_from', 'date_to')
    def onchange_date_to(self):
        for each in self:
            if each.date_from > each.date_to:
                raise Warning('Date To must be greater than Date From')

    @api.onchange('date_from', 'date_to')
    def check_availability(self):
        if self.date_from and self.date_to:
            self.fleet = ''
            fleet_obj = self.env['fleet.vehicle'].search([])
            for i in fleet_obj:
                for each in i.reserved_time:
                    if each.date_from <= self.date_from <= each.date_to:
                        i.write({'check_availability': False})
                    elif self.date_from < each.date_from:
                        if each.date_from <= self.date_to <= each.date_to:
                            i.write({'check_availability': False})
                        elif self.date_to > each.date_to:
                            i.write({'check_availability': False})
                        else:
                            i.write({'check_availability': True})
                    else:
                        i.write({'check_availability': True})

    reserved_fleet_id = fields.Many2one('employee.fleet.reserved', invisible=1, copy=False)
    name = fields.Char(string='Request Number', copy=False)
    employee = fields.Many2one('hr.employee', string='Employee', required=1, readonly=True,
                               states={'new': [('readonly', False)]})
    req_date = fields.Datetime(string='Requested Date', readonly=True)
    confirm_date = fields.Datetime(string='Confirm Date', readonly=True)
    assigned_date = fields.Datetime(string='Assigned Date', readonly=True)
    returned_date_time = fields.Datetime(string='Return Date', readonly=True)
    fleet = fields.Many2one('fleet.vehicle', string='Vehicle', readonly=True, required=1,
                            states={'new': [('readonly', False)]})
    date_from = fields.Date(string='Date From', required=1, readonly=True,
                            states={'new': [('readonly', False)]})
    date_to = fields.Date(string='Date To', required=1, readonly=True,
                          states={'new': [('readonly', False)]})
    returned_date = fields.Datetime(string='Returned Date', readonly=1)
    purpose = fields.Html(string='Purpose', required=1,
                          states={'new': [('readonly', False)]}, help="Purpose")
    state = fields.Selection([('new', 'New'),
                              ('confirmed', 'Confirmed'),
                              ('approved', 'Approved'),
                              ('assigned', 'Assigned'),
                              ('returned', 'Returned')],
                             string="State", default="new",
                             tracking=True)
    department_id = fields.Many2one(related='employee.department_id', string='Department',
                                    ondelete='set null',
                                    index="True")
    project_id = fields.Many2one('project.project', string='Project', readonly=True,
                                 states={'new': [('readonly', False)]})
    task_id = fields.Many2one('project.task', string='Task', readonly=True,
                              states={'new': [('readonly', False)]})

    def confirm_action(self):
        self.state = 'confirmed'
        self.confirm_date = datetime.today()

    def approved_action(self):
        self.state = 'approved'

    def assigned_action(self):
        self.state = 'assigned'
        self.assigned_date = datetime.today()

    def returned_action(self):
        self.state = 'returned'
        self.returned_date_time = datetime.today()


class employeeInherit(models.Model):
    _inherit = 'hr.employee'

    test_count = fields.Integer(compute="_compute_count_all", string="Vehicle History Count")

    def _compute_count_all(self):
        for record in self:
            record.test_count = self.env['employee.fleet'].search_count(
                [('employee', '=', record.name), ('state', '=', "assigned")])
