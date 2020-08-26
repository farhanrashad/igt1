# -*- coding: utf-8 -*-
# from odoo import http


# class OhEmployeeCheckList(http.Controller):
#     @http.route('/oh_employee_check_list/oh_employee_check_list/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oh_employee_check_list/oh_employee_check_list/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oh_employee_check_list.listing', {
#             'root': '/oh_employee_check_list/oh_employee_check_list',
#             'objects': http.request.env['oh_employee_check_list.oh_employee_check_list'].search([]),
#         })

#     @http.route('/oh_employee_check_list/oh_employee_check_list/objects/<model("oh_employee_check_list.oh_employee_check_list"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oh_employee_check_list.object', {
#             'object': obj
#         })
