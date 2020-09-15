# -*- coding: utf-8 -*-

from odoo import api, fields, models


class HrLeaveExt(models.Model):
    _inherit = 'hr.leave'

    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.uid, readonly=True)
