from odoo import http
from odoo.http import request

class JobListingController(http.Controller):

    @http.route('/jobs', type='http', auth='public', website=True)
    def job_list(self, **kwargs):
        jobs = request.env['scraped.job'].sudo().search([])
        return request.render('scraped_content.job_listing_template', {
            'jobs': jobs
        })
