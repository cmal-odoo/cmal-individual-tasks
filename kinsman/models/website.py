from odoo import models, fields

class Website(models.Model):
    _inherit = 'website'
    is_hide_price = fields.Boolean(string="Hide cart and prices")

