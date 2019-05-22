# -*- coding: utf-8 -*-
from odoo import http

# class ControlesData(http.Controller):
#     @http.route('/controles_data/controles_data/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/controles_data/controles_data/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('controles_data.listing', {
#             'root': '/controles_data/controles_data',
#             'objects': http.request.env['controles_data.controles_data'].search([]),
#         })

#     @http.route('/controles_data/controles_data/objects/<model("controles_data.controles_data"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('controles_data.object', {
#             'object': obj
#         })