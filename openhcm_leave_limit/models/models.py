# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrLeave(models.Model):
    _inherit = 'hr.leave'



    # name = fields.Char('Leave type')
    meeting = fields.Char('Meeting type')
    apply = fields.Boolean("Apply Double Validation")
    limit = fields.Boolean("Allow to Override Limit")
    report = fields.Char('Color in Report')

    leave_limit = fields.Boolean("Monthly Leave Limit")
    limit_days = fields.Float('Leave Limit Days', deafult=13)


# class LeaveRequest(models.Model):
#     _name = 'leave.request'
#
#     name = fields.Char('Description')
#     leave_type = fields.Char('Leave type')
#     date = fields.Date(string='Duration', required=False)
#     mode = fields.Char('Mode')
#     employee_id = fields.Many2one('hr.employee', 'Employee')
#     department_id = fields.Many2one('hr.employee', 'Department')
#     decision = fields.Html(string='Comment by Manager')














