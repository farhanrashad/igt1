# -*- coding: utf-8 -*-

from odoo import api, fields, models


class VisitDuration(models.Model):
    _name = "visit.duration"

    name= fields.Char(string='Name',required=True)
    dur_code=fields.Char(string='Code')


