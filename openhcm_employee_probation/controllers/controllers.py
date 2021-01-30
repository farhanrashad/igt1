# -*- coding: utf-8 -*-
# from odoo import http


# class OpenhcmEmployeeProbation(http.Controller):
#     @http.route('/openhcm_employee_probation/openhcm_employee_probation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openhcm_employee_probation/openhcm_employee_probation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openhcm_employee_probation.listing', {
#             'root': '/openhcm_employee_probation/openhcm_employee_probation',
#             'objects': http.request.env['openhcm_employee_probation.openhcm_employee_probation'].search([]),
#         })

#     @http.route('/openhcm_employee_probation/openhcm_employee_probation/objects/<model("openhcm_employee_probation.openhcm_employee_probation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openhcm_employee_probation.object', {
#             'object': obj
#         })
