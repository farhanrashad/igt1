# -*- coding: utf-8 -*-

from odoo import api, fields, models

class VisitCategory(models.Model):
    _name = "visit.category"


    name= fields.Char(string='Name',required=True)
    cat_code=fields.Char(string='Code')


