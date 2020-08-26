# -*- coding: utf-8 -*-
# from odoo import http


# class OhEmployeeDocumentsExpiry(http.Controller):
#     @http.route('/oh_employee_documents_expiry/oh_employee_documents_expiry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oh_employee_documents_expiry/oh_employee_documents_expiry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oh_employee_documents_expiry.listing', {
#             'root': '/oh_employee_documents_expiry/oh_employee_documents_expiry',
#             'objects': http.request.env['oh_employee_documents_expiry.oh_employee_documents_expiry'].search([]),
#         })

#     @http.route('/oh_employee_documents_expiry/oh_employee_documents_expiry/objects/<model("oh_employee_documents_expiry.oh_employee_documents_expiry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oh_employee_documents_expiry.object', {
#             'object': obj
#         })
