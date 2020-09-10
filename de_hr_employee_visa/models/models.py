# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _name = 'hr.employee'

    visa_lines = fields.One2many('visa.card.details', 'visa_id')

    passport_number = fields.Char(String="Passport Number")
    passport_issue_date = fields.Date(String="Passport Issue Date")
    passport_expiry_date = fields.Date(String="Passport Expiry Date")
    passport_country = fields.Many2one('res.country', String="Passport Expiry Date")
    other_nationality = fields.Many2many('res.country', string="Other Nationality")


class VisaCardDetails(models.Model):
    _name = 'visa.card.details'
    _description = 'Visa Card Details'

    @api.onchange('employee_id', 'visa_Type')
    def onchange_des(self):
        if self.employee_id and self.visa_Type:
            self.description = str(self.visa_Type.name) + str(self.employee_id.name)

    state = fields.Selection(
        [('to_request', 'To Request'), ('in_process', 'In Process'), ('approve', 'Approve'), ('reject', 'Reject'),
         ('expired', 'Expired')], string='status', default='to_request')
    visa_id = fields.Many2one('hr.employee', String="Visa Id")
    employee_id = fields.Many2one('hr.employee', String="Employee")
    description = fields.Char(string="Description")
    visa_Type = fields.Many2one('visa.card.type', String="Visa Type",  required=1)
    Visa_issuance_Date = fields.Date(string="Issuance Date", required=1)
    Visa_Expiration_Date = fields.Date(string="Expiration Date", required=1)
    Visa_country = fields.Many2one('res.country', string="Country", required=1)
    no_of_entries = fields.Selection([('single_entry_visa', 'Single Entry Visa'),
                                      ('double_entry_visa', 'Double Entry Visa'),
                                      ('multiple_entry_visa', 'Multiple Entry Visa')])
    status = fields.Char(string="Status")

    def to_request(self):
        self.state = 'in_process'

    def approve_action(self):
        self.state = 'approve'

    def reject_action(self):
        self.state = 'reject'

    def expired_action(self):
        self.state = 'expired'


class VisaCardType(models.Model):
    _name = 'visa.card.type'

    name = fields.Char(String="Visa Type", required=1)
