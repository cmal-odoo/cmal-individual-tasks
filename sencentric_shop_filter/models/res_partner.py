from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_ids = fields.One2many('product.product', 'id', string='Visible Products')