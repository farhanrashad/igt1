
from odoo import api, fields, models, _


class Orientation(models.Model):
    _name = 'employee.orientation'
    _description = "Employee Orientation"
    _inherit = 'mail.thread'

    name = fields.Char(string='Employee Orientation', readonly=True, default=lambda self: _('New'))
    employee_name = fields.Many2one('hr.employee', string='Employee', size=32, required=True)
    department = fields.Many2one('hr.department', string='Department',
                                 required=True)
    date = fields.Datetime(string="Date")
    # date = fields.Datetime.to_string(dateText)
    responsible_user = fields.Many2one('res.users', string='Responsible User')
    employee_company = fields.Many2one('res.company', string='Company', required=True,
                                       default=lambda self: self.env.user.company_id)
    parent_id = fields.Many2one('hr.employee', string='Manager')
    job_id = fields.Many2one('hr.job', string='Job Title', related='employee_name.job_id',
                             domain="[('department_id', '=', department)]")
    orientation_id = fields.Many2one('employee.orientation.checklist', string='Orientation Checklist',
                                     domain="[('checklist_department','=', department)]", required=True)
    note_id = fields.Text('Description')
    orientation_request = fields.One2many('employee.orientation.request', 'request_orientation', string='Orientation Request')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Canceled'),
        ('complete', 'Completed'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

    def confirm_orientation(self):
        self.write({'state': 'confirm'})
        for values in self.orientation_id.checklist_line_id:
            self.env['employee.orientation.request'].create({
                'request_name': values.line_name,
                'request_orientation': self.id,
                'partner_id': values.responsible_user.id,
                'request_date': self.date,
                'employee_id': self.employee_name.id,
            })

    def cancel_orientation(self):
        for request in self.orientation_request:
            request.state = 'cancel'
        self.write({'state': 'cancel'})

    def complete_orientation(self):
        force_complete = False
        for request in self.orientation_request:
            if request.state == 'new':
                force_complete = True
        if force_complete:
            return {
                'name': 'Complete Orientation',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'employee.orientation.force.complete',
                'type': 'ir.actions.act_window',
                'context': {'default_orientation_id': self.id},
                'target': 'new',
            }
        self.write({'state': 'complete'})

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('employee.orientation')
        result = super(Orientation, self).create(vals)
        return result
