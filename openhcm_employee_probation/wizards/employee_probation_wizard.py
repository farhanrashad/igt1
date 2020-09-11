# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class EmployeeProbationWizard(models.TransientModel):
    _name = "employee.probation.wizard"
    _description = "hr.employee.probation.wizard"

    add_review = fields.Text(string='Add Review')
    current_id = fields.Integer()

    def send_review(self):
        text = ''
        self.model = self.env.context.get('active_model')
        rec = self.env[self.model].browse(self.env.context.get('active_id'))
        text = rec.get_review
        if text:
            text = str(text)+(self.add_review + '\n')
            rec.get_review = str(text)
        else:
            rec.get_review = (self.add_review + '\n')

        print('___context id', self._context['current_id'])
