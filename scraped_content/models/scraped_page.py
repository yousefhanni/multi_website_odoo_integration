from odoo import models, fields

class ScrapedPage(models.Model):
    _name = 'scraped.page'
    _description = 'Scraped Page'

    title = fields.Char(string="Page Title", required=True)
    content = fields.Text(string="Page Content")
    source_url = fields.Char(string="Source URL")
    status = fields.Selection([
        ('new', 'New'),
        ('in_review', 'In Review'),
        ('approved', 'Approved'),
        ('archived', 'Archived')
    ], default='new')
