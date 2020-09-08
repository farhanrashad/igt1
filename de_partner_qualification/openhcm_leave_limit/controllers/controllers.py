# -*- coding: utf-8 -*-
# from odoo import http


# class OpenhcmLeaveLimit(http.Controller):
#     @http.route('/openhcm_leave_limit/openhcm_leave_limit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openhcm_leave_limit/openhcm_leave_limit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openhcm_leave_limit.listing', {
#             'root': '/openhcm_leave_limit/openhcm_leave_limit',
#             'objects': http.request.env['openhcm_leave_limit.openhcm_leave_limit'].search([]),
#         })

#     @http.route('/openhcm_leave_limit/openhcm_leave_limit/objects/<model("openhcm_leave_limit.openhcm_leave_limit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openhcm_leave_limit.object', {
#             'object': obj
#         })
