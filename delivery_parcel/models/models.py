# -*- coding: utf-8 -*-
##

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ProductPackaging(models.Model):
    _inherit = 'product.packaging'

    package_carrier_type = fields.Selection(selection_add=[('parcel', 'Parcel')])

class delivery_parcel(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(selection_add=[('parcel', 'Parcel')])
    parcel_username = fields.Char(string='Parcel Username')
    parcel_passwd = fields.Char(string='Parcel Password')
    parcel_access_number = fields.Char(string='Parcel AccessLicenseNumber')
    parcel_package_weight_unit = fields.Selection([('LBS', 'Pounds'), ('KGS', 'Kilograms')], default='LBS' ,string='Parcel Package Weight Unit')
    parcel_package_dimension_unit = fields.Selection([('IN', 'Inches'), ('CM', 'Centimeters')], string="Units for Parcel Package Size", default='IN')
    parcel_label_file_type = fields.Selection([('GIF', 'PDF'),
                                            ('ZPL', 'ZPL'),
                                            ('EPL', 'EPL'),
                                            ('SPL', 'SPL')],
                                           string="Parcel Label File Type", default='GIF', oldname='x_label_file_type')
