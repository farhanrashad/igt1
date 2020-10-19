from odoo import http
from odoo.http import request
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo.addons.website_sale.controllers.main import WebsiteSale


def leave_page_content():
    leave_type = request.env['hr.leave.type'].search([])
    employees = request.env['hr.employee'].search([])
    users = request.env['res.users'].search([])
    default_user_id = request.env.user.id
    print('user', request.env.user.id)
    login_user = request.env['res.users'].search([('id', '=', request.env.user.id)])
    email = login_user.login
    return {
        'leave_type': leave_type,
        'employees': employees,
        'users': users,
        'default_user_id': default_user_id,
        'email': email
    }


class MyLeaves(http.Controller):

    @http.route('/leave_page', type="http", auth="user", website=True)
    def leave_template(self, **kw):
        print("Execution Here.........................", kw)
        user = request.env.user.id
        employee = request.env['hr.employee'].search([('user_id', '=', user)])
        if employee:
            return http.request.render('de_employee_leave_request.leave_template', leave_page_content())
        else:
            raise UserError(_("You are not allowed to modify this data."))
        # leave_type = int(kw.get('holiday_status_id'))
        # leave_category = request.env['hr.leave.type'].search([('id', '=', leave_type)])
        # emp_id = int(kw.get('employee_id'))
        # leave_days = leave_category.get_days(emp_id)[leave_type]
        # print('days', leave_days)
        # remaining_leave = leave_days['remaining_leaves']
        # return http.request.render('de_employee_leave_request.leave_template', leave_page_content())

    @http.route('/my_leave_page', type="http", auth="user", website=True)
    def leave_page_template(self, **kw):
        print("leave Execution Here.........................", request.env.user.name, request.env.user.id)
        leave_details = request.env['hr.leave'].sudo().search([('user_id', '=', request.env.user.id)])
        return request.render('de_employee_leave_request.leave_page_template', {'my_details': leave_details})

    @http.route('/create/leave', type="http", auth="public", website=True)
    def create_leave(self, **kw):
        print("Data Received.....", kw)
        fmt = '%Y-%m-%d'
        date_from = kw.get('request_date_from')
        date_to = kw.get('request_date_to')
        d1 = datetime.strptime(date_from, fmt)
        d2 = datetime.strptime(date_to, fmt)
        days_diff = float((d2 - d1).days)
        leave_type = int(kw.get('holiday_status_id'))
        emp_id = int(kw.get('employee_id'))
        total_leaves = request.env['hr.leave.allocation'].search_count([('holiday_status_id', '=', leave_type),
                                                                        ('employee_id', '=', emp_id)])
        # total_leaves = count(total_leaves)
        allocated_leaves = request.env['hr.leave'].search_count([('holiday_status_id', '=', leave_type), ('employee_id', '=', emp_id),
                                                                ('state', '=', 'validate')])
        remaining_leaves = total_leaves - allocated_leaves
        print('remaining', remaining_leaves)
        leave_category = request.env['hr.leave.type'].search([('id', '=', leave_type)])
        leave_days = leave_category.get_days(emp_id)[leave_type]
        days = leave_days['remaining_leaves']
        print('days', days)
        print('new', leave_category.get_days(emp_id))
        print('leave_type', leave_type)
        print('remaining', leave_days)
        print('requested', days_diff)
        # remaining_leave = leave_days['remaining_leaves']
        if days_diff > days:
            raise ValidationError(_('The number of remaining time off is not sufficient for this time off type.'))
        doctor_val = {
            'holiday_status_id': int(kw.get('holiday_status_id')),
            'employee_id': int(kw.get('employee_id')),
            'request_date_from': kw.get('request_date_from'),
            'request_date_to': kw.get('request_date_to'),
            'number_of_days': days_diff,
            'user_id': request.env.user.id,
            'name': kw.get('name'),
        }
        leave_record = request.env['hr.leave'].sudo().create(doctor_val)
        return request.render("de_employee_leave_request.patient_thanks", {})

