# -*- coding: utf-8 -*-
# from odoo import http


# class Exoplanet(http.Controller):
#     @http.route('/exoplanet/exoplanet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exoplanet/exoplanet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exoplanet.listing', {
#             'root': '/exoplanet/exoplanet',
#             'objects': http.request.env['exoplanet.exoplanet'].search([]),
#         })

#     @http.route('/exoplanet/exoplanet/objects/<model("exoplanet.exoplanet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exoplanet.object', {
#             'object': obj
#         })
