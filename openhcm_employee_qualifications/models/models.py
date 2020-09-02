# -- coding: utf-8 --
import datetime
from odoo import api, fields, models, _
from odoo.tools import float_compare
from odoo.exceptions import UserError, ValidationError, Warning

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    # foreign key comcept
    experience_lines = fields.One2many('hr.employee.work.experience', 'experience_id', string='Employee Experince line',
                                       readonly=True,
                                       copy=True, auto_join=True)

    skill_lines = fields.One2many('hr.employee.skill', 'skill_id', string='Employee skill line',
                                       readonly=True,
                                       copy=True, auto_join=True)

    language_lines = fields.One2many('hr.employee.language', 'language_id', string='Employee language line',
                                  readonly=True,
                                  copy=True, auto_join=True)

    education_lines = fields.One2many('hr.employee.education', 'education_id', string='Employee education line',
                                  readonly=True,
                                  copy=True, auto_join=True)

    license_lines = fields.One2many('hr.employee.license', 'license_id', string='Employee education line',
                                  readonly=True,
                                  copy=True, auto_join=True)

    attachment_lines = fields.One2many('hr.employee.attachment', 'attachment_id', string='Employee education line',
                                  readonly=True,
                                  copy=True, auto_join=True)


class HrEmployeeWorkExperience(models.Model):
    _name = 'hr.employee.work.experience'
    _description = 'Employee Work'
    company = fields.Char(string='company', store=True, required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', store=True)
    job_title = fields.Char(string='Job Title', store=True)
    From = fields.Integer(string='from', store=True)
    To = fields.Integer(string='To', store=True, required=True)
    comments = fields.Text(string="Comments")
    experience_id = fields.Many2one('hr.employee', string='experience id', index=True, required=True,
                                          ondelete='cascade')

class HrEmployeeSkill(models.Model):
    _name = 'hr.employee.skill'
    _description = 'Employee skill'
    skill_id = fields.Many2one('hr.employee', string='skill',index=True, required=True,
                                          ondelete='cascade')
    skill = fields.Char(string='Skill', store=True, required=True)
    years_of_experience = fields.Char(string='Years OF Experience', store=True, required=True)


class HrEmployeeLanguage(models.Model):
    _name = 'hr.employee.language'
    _description = 'Employee Language'
    language_id = fields.Many2one('hr.employee', string='language_id',index=True, required=True,
                                          ondelete='cascade')
    language = fields.Char(string='language', store=True, required=True)
    fluency = fields.Char(string='Fluency', store=True, required=True)
    competency = fields.Char(string='Competency', store=True, required=True)
    comments = fields.Char(string='Comments', store=True, required=True)

class HrEmployeeEducation(models.Model):
    _name = 'hr.employee.education'
    _description = 'Employee Education'
    education_id = fields.Many2one('hr.employee', string='education_id',index=True, required=True,
                                          ondelete='cascade')
    level = fields.Char(string='level', store=True, required=True)
    year = fields.Char(string='year', store=True, required=True)
    cgpa_score = fields.Char(string='CGPA/score', store=True, required=True)


class HrEmployeeLicense(models.Model):
    _name = 'hr.employee.license'
    _description = 'Employee License'
    license_id = fields.Many2one('hr.employee', string='education_id',index=True, required=True,
                                          ondelete='cascade')
    license_type = fields.Char(string='licese Type', store=True, required=True)
    issue_date = fields.Date(string='issue date', store=True, required=True)
    expiry_date = fields.Date(string='expiry date', store=True, required=True)


class HrEmployeeAttachment(models.Model):
    _name = 'hr.employee.attachment'
    _description = 'Employee attachment'
    attachment_id = fields.Many2one('hr.employee', string='attachment_id',index=True, required=True,
                                          ondelete='cascade')
    attachment = fields.Binary(string="My Attachment", attachment=True)

class HrEmployeeFamily(models.Model):
    _name = 'hr.employee.family'
    _description = 'Employee family'
    family_id = fields.Many2one('hr.employee', string='family_id',index=True, required=True,
                                          ondelete='cascade')
    family_Owner = fields.Char(string='Owner Name', store=True, required=True)
    Totalmember = fields.Char(string='total member', store=True, required=True)
