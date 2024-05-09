# -*- coding: utf-8 -*-
from odoo import http


class M10test(http.Controller):
    @http.route('/m10test/m10test', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/m10test/m10test/objects', auth='public')
    def list(self, **kw):
        return http.request.render('m10test.listing', {
            'root': '/m10test/m10test',
            'objects': http.request.env['m10test.m10test'].search([]),
        })

    @http.route('/m10test/m10test/objects/<model("m10test.m10test"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('m10test.object', {
            'object': obj
        })
