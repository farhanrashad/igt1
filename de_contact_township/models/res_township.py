# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ContactTownship(models.Model):
    _name = 'res.townships'
    _description = 'This is Township model'

    city = fields.Char(string="City", required=True)
    name = fields.Char(string="Name",required=True)

    

class ResContact(models.Model):
    _inherit = 'res.partner' 
    
    township_id = fields.Many2one('res.townships', string="Township")