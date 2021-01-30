# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import datetime


class VisitDetail(models.Model):
    _name = "visit.detail"

#   Making necessary states
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in', 'In'),
        ('out', 'Out')
    ], readonly=True, index=True, copy=False)

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
    check_in=fields.Datetime(string="Check In",readonly=True)
    check_out=fields.Datetime(string="Check Out",readonly=True)

#     declairing group for Contact Details
    reference_id=fields.Many2one("hr.employee",string="Reference")
    department_id=fields.Many2one("hr.employee",string="Department")
    employee_id=fields.Many2one("hr.department",string="Employee")

#   declaring comment for notebook
    comment=fields.Html()
#     sequence generation
    name=fields.Char(string="Visitor Sequence",required=True,copy=False,readonly=True,index=True,default=lambda self: _('New'))

    # @api.model
    # def write(self, vals):
    #     print("write----")
    #     vals['state'] = 'draft'
    #     return super(VisitDetail, self).write(vals)

    # adding new field total duration
    total_duration = fields.Float(string="Total Duration")

    @api.onchange('check_in','check_out')
    def _get_total_duration(self):
        print("printing difference ",self.check_out-self.check_in)
        if self.check_in:
            f =self.check_out
            s = self.check_in
            q = f - s
            d_s = q.total_seconds()
            print("in seconds----", d_s)
            hours = divmod(d_s, 3600)[0]
            print(type(hours))
            self.total_duration=float(hours)
        else:
            return



    @api.model
    def create(self,vals):
        vals['state'] = 'draft'
        print("called",vals['state'])
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('visitor.sequence') or _('New')
        result = super(VisitDetail, self).create(vals)
        return result

    # defining actions for states
    def set_checkIn(self):
        self.state='in'
        self.check_in=datetime.datetime.today()


    def set_checkOut(self):
        self.state = 'out'
        self.check_out=datetime.datetime.today()