# -*- coding: utf-8 -*-
# from odoo import http


# class OpenhcmEmployeeQualifications(http.Controller):
#     @http.route('/openhcm_employee_qualifications/openhcm_employee_qualifications/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openhcm_employee_qualifications/openhcm_employee_qualifications/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openhcm_employee_qualifications.listing', {
#             'root': '/openhcm_employee_qualifications/openhcm_employee_qualifications',
#             'objects': http.request.env['openhcm_employee_qualifications.openhcm_employee_qualifications'].search([]),
#         })

#     @http.route('/openhcm_employee_qualifications/openhcm_employee_qualifications/objects/<model("openhcm_employee_qualifications.openhcm_employee_qualifications"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openhcm_employee_qualifications.object', {
#             'object': obj
#         })
