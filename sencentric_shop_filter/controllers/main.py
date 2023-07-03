from odoo import http

class WebsiteSale(http.Controller):
    @http.route('/shop', auth='public', website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(WebsiteSale, self).shop(page, category, search, ppg, **post)
        # Check if the user is authenticated and is a portal user
        if not http.request.env['res.users'].browse(http.request.session.uid).has_group('base.group_portal'):
            # If not, redirect them to the login page
            return http.request.redirect('/web/login')
        # Otherwise, proceed as usual
        return res
        
