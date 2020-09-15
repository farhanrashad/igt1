# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class de_hr_leave_summary(models.Model):
#     _name = 'de_hr_leave_summary.de_hr_leave_summary'
#     _description = 'de_hr_leave_summary.de_hr_leave_summary'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
