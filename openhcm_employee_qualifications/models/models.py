# -- coding: utf-8 --
import datetime
from odoo import api, fields, models, _
from odoo.tools import float_compare
from odoo.exceptions import UserError, ValidationError, Warning

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    # foreign key concept
    experience_lines = fields.One2many('hr.employee.work.experience', 'experience_id', string='Employee Experince line',copy=True, auto_join=True)

    skill_lines = fields.One2many('hr.employee.skill', 'skill_id', string='Employee skill line',copy=True, auto_join=True)

    language_lines = fields.One2many('hr.employee.language', 'language_id', string='Employee language line',

                                  copy=True, auto_join=True)

    education_lines = fields.One2many('hr.employee.education', 'education_id', string='Employee education line',

                                  copy=True, auto_join=True)

    license_lines = fields.One2many('hr.employee.license', 'license_id', string='Employee education line',

                                  copy=True, auto_join=True)

    attachment_lines = fields.One2many('hr.employee.attachment', 'attachment_id', string='Employee education line',

                                  copy=True, auto_join=True)

    family_lines = fields.One2many('hr.employee.family', 'family_id', string='Employee family line')


    contact_lines = fields.One2many('hr.employee.contact.detail', 'contact_id', string='Employee contact line')


    dependents_lines = fields.One2many('hr.employee.dependent', 'dependent_id', string='Employee dependent line')



class HrEmployeeWorkExperience(models.Model):
    _name = 'hr.employee.work.experience'
    _description = 'Work'
    company = fields.Char(string='Company', store=True, required=True)
    job_title = fields.Char(string='Job Title', store=True)
    From = fields.Date(string='From')
    To = fields.Date(string='To')
    comments = fields.Text(string="Comments")
    experience_id = fields.Many2one('hr.employee', string='Experience Id', index=True, required=True,
                                          ondelete='cascade')

class HrEmployeeSkill(models.Model):
    _name = 'hr.employee.skill'
    _description = 'Skill'
    skill_id = fields.Many2one('hr.employee', string='skill',index=True, required=True,
                                          ondelete='cascade')
    skill = fields.Char(string='Skill', store=True, required=True)
    years_of_experience = fields.Float(string='Years Of Experience', type="float", store=True, required=True)

# language select option
language_fluency_choices = (
    ('Native','Native'),
    ('Basic', 'Basic'),
    ('Fluent','Fluent'),
)
class HrEmployeeLanguage(models.Model):
    _name = 'hr.employee.language'
    _description = 'Employee Language'
    language_id = fields.Many2one('hr.employee', string='language_id',index=True, required=True,
                                          ondelete='cascade')
    language = fields.Char(string='Language', store=True, required=True)
    fluency = fields.Selection([('Native','Native'),('Basic','Basic'),('Fluent','Fluent'),], default='Native', tracking=True)
    competency = fields.Char(string='Competency', store=True)
    comments = fields.Char(string='Comments', store=True)


class HrEmployeeEducation(models.Model):
    _name = 'hr.employee.education'
    _description = 'Employee Education'
    education_id = fields.Many2one('hr.employee', string='education_id',index=True, required=True,
                                          ondelete='cascade')
    level = fields.Selection([('shs', 'Some High School'),
                              ('hsd', 'High School Diploma/GED'),
                              ('sc', 'Some College'),
                              ('ad', ' Associate Degree'),
                              ("bd", "Bachelor's Degree"),
                              ('md', "Master's Degree Or Higher")],
                              default='bd')
    year = fields.Char(string='Year', store=True, required=True)
    cgpa_score = fields.Char(string='CGPA/Score', store=True, required=True)


class HrEmployeeLicense(models.Model):
    _name = 'hr.employee.license'
    _description = 'Employee License'
    license_id = fields.Many2one('hr.employee', string='education_id',index=True, required=True,
                                          ondelete='cascade')
    license_type = fields.Char(string='License Type', store=True, required=True)
    issue_date = fields.Date(string='Issue Date', store=True, required=True)
    expiry_date = fields.Date(string='Expiry Date', store=True, required=True)


class HrEmployeeAttachment(models.Model):
    _name = 'hr.employee.attachment'
    _description = 'Employee attachment'
    attachment_id = fields.Many2one('hr.employee', string='attachment_id',index=True, required=True,
                                          ondelete='cascade')
    attachment = fields.Binary(string="Attach File", attachment=True)

class HrEmployeeFamily(models.Model):
    _name = 'hr.employee.family'
    _description = 'Employee family'
    family_id = fields.Many2one('hr.employee', string='family_id',index=True, required=True,
                                          ondelete='cascade')
    family_Owner = fields.Char(string='Owner Name', store=True, required=True)
    Totalmember = fields.Char(string='total Member', store=True, required=True)


class HrEmployeeDependent(models.Model):
    _name = 'hr.employee.dependent'
    _description = 'Employee Dependent'
    dependent_id = fields.Many2one('hr.employee', string='Dependent Id',index=True, required=True,
                                          ondelete='cascade')
    name = fields.Char(string='Name', store=True, required=True)
    date_Of_birth = fields.Date(string='DOB', store=True, required=True)
    relationship = fields.Selection([('parent', 'Parent'),
                              ('gparent', 'Grand Parent'),
                              ('sib', 'Sibling'),
                              ('husb', 'Husband'),
                              ("wife", "Wife")],
                             default='parent')

class HrEmployeeContactDetail(models.Model):
    _name = 'hr.employee.contact.detail'
    _description = 'Employee contact'
    contact_id = fields.Many2one('hr.employee', string='Contact Detail',index=True, required=True,
                                          ondelete='cascade')
    adress_stree_1 = fields.Text(string='Address', store=True, required=True)
    state = fields.Many2one("res.country.state", string='State', help='Enter State', ondelete='restrict')
    country = fields.Many2one('res.country', string='Country', help='Select Country', ondelete='restrict')
    city = fields.Char(string='Mobile Number', store=True, required=True)
    zip_code = fields.Char(string='Zip/Postal code', store=True, required=True)
    home_Telephone = fields.Integer(string='Home Contact', store=True, required=True)
    work_Telephone = fields.Integer(string='Work Contact', store=True, required=True)
    mobile = fields.Integer(string='Personal Number', store=True, required=True)
    work_email = fields.Char(string='Work Email', store=True, required=True)
    other_email = fields.Char(string='Other Email', store=True, required=True)