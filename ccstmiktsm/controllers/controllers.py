# -*- coding: utf-8 -*-
# from odoo import http


# class Ccstmiktsm(http.Controller):
#     @http.route('/ccstmiktsm/ccstmiktsm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ccstmiktsm/ccstmiktsm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ccstmiktsm.listing', {
#             'root': '/ccstmiktsm/ccstmiktsm',
#             'objects': http.request.env['ccstmiktsm.ccstmiktsm'].search([]),
#         })

#     @http.route('/ccstmiktsm/ccstmiktsm/objects/<model("ccstmiktsm.ccstmiktsm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ccstmiktsm.object', {
#             'object': obj
#         })
