from odoo import http
from odoo.http import request

class PriceController(http.Controller):
    @http.route(['/toggle_hide_prices'], type='json', auth="user", website=True)
    def toggle_hide_prices(self, **kwargs):
        website = request.website
        website.is_hide_price = not website.is_hide_price
        return {'status': 'success'}
