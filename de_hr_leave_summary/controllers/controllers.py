# -*- coding: utf-8 -*-
# from odoo import http


# class DeHrLeaveSummary(http.Controller):
#     @http.route('/de_hr_leave_summary/de_hr_leave_summary/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de_hr_leave_summary/de_hr_leave_summary/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de_hr_leave_summary.listing', {
#             'root': '/de_hr_leave_summary/de_hr_leave_summary',
#             'objects': http.request.env['de_hr_leave_summary.de_hr_leave_summary'].search([]),
#         })

#     @http.route('/de_hr_leave_summary/de_hr_leave_summary/objects/<model("de_hr_leave_summary.de_hr_leave_summary"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de_hr_leave_summary.object', {
#             'object': obj
#         })
