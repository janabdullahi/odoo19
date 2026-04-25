# -*- coding: utf-8 -*-
# from odoo import http


# class MyModule(http.Controller):
#     @http.route('/my__module/my__module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my__module/my__module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my__module.listing', {
#             'root': '/my__module/my__module',
#             'objects': http.request.env['my__module.my__module'].search([]),
#         })

#     @http.route('/my__module/my__module/objects/<model("my__module.my__module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my__module.object', {
#             'object': obj
#         })

