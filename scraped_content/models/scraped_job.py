from odoo import models, fields

class ScrapedJob(models.Model):
    _name = 'scraped.job'
    _description = 'Scraped Job'

    name = fields.Char(string="Job Title", required=True)
    company_name = fields.Char(string="Company Name")
    company_logo_url = fields.Char(string="Company Logo URL")
    location = fields.Char(string="Location")
    source_url = fields.Char(string="Source URL")
    date_posted = fields.Char(string="Date Posted")
    status = fields.Selection([
        ('new', 'New'),
        ('in_review', 'In Review'),
        ('approved', 'Approved'),
        ('archived', 'Archived')
    ], default='new')
