# -*- coding: utf-8 -*-
# from odoo import http


# class IspProject(http.Controller):
#     @http.route('/isp_project/isp_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/isp_project/isp_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('isp_project.listing', {
#             'root': '/isp_project/isp_project',
#             'objects': http.request.env['isp_project.isp_project'].search([]),
#         })

#     @http.route('/isp_project/isp_project/objects/<model("isp_project.isp_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('isp_project.object', {
#             'object': obj
#         })

