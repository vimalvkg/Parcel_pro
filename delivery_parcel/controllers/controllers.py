# -*- coding: utf-8 -*-
from odoo import http

# class DeliveryParcel(http.Controller):
#     @http.route('/delivery_parcel/delivery_parcel/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delivery_parcel/delivery_parcel/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delivery_parcel.listing', {
#             'root': '/delivery_parcel/delivery_parcel',
#             'objects': http.request.env['delivery_parcel.delivery_parcel'].search([]),
#         })

#     @http.route('/delivery_parcel/delivery_parcel/objects/<model("delivery_parcel.delivery_parcel"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delivery_parcel.object', {
#             'object': obj
#         })