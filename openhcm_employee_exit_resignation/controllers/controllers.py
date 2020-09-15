# -*- coding: utf-8 -*-
# from odoo import http


# class OpenhcmEmployeeExitResignation(http.Controller):
#     @http.route('/openhcm_employee_exit_resignation/openhcm_employee_exit_resignation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openhcm_employee_exit_resignation/openhcm_employee_exit_resignation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openhcm_employee_exit_resignation.listing', {
#             'root': '/openhcm_employee_exit_resignation/openhcm_employee_exit_resignation',
#             'objects': http.request.env['openhcm_employee_exit_resignation.openhcm_employee_exit_resignation'].search([]),
#         })

#     @http.route('/openhcm_employee_exit_resignation/openhcm_employee_exit_resignation/objects/<model("openhcm_employee_exit_resignation.openhcm_employee_exit_resignation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openhcm_employee_exit_resignation.object', {
#             'object': obj
#         })
