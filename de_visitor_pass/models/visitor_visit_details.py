# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class VisitDetail(models.Model):
    _name = "visit.detail"

#   declaring fieldss for 1 group visitorr details
    det_name= fields.Char(string='Name',required=True)
    det_company=fields.Char(string='Company')
    phone_no=fields.Char(string='Phone')
    mail=fields.Char(string='Mail')

#     declaring fields for 2 group visit details
    des=fields.Char("Visit Destination")
    dur=fields.Many2one("visit.duration",string="Visit Duration")
    cat=fields.Many2one("visit.category",string="Visitor Category")

#   declaring group for  checkin check out
    check_in=fields.Datetime(string="Check In",required=True)
    check_out=fields.Datetime(string="Check Out")

#     declairing group for Contact Details
    reference_id=fields.Many2one("hr.employee",string="Reference")
    department_id=fields.Many2one("hr.department",string="Department")
    employee_id=fields.Many2one("hr.employee",string="Employee")

#   declaring comment for notebook
    comment=fields.Text(string="Add Comment")

#     sequence generation
    name=fields.Char(string="Visitor Sequence",required=True,copy=False,readonly=True,index=True,default=lambda self: _('New'))

    @api.model
    def create(self,vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('visitor.sequence') or _('New')
        result = super(VisitDetail, self).create(vals)
        return result