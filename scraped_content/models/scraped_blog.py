from odoo import models, fields

class ScrapedBlog(models.Model):
    _name = 'scraped.blog'
    _description = 'Scraped Blog'

    title = fields.Char(string="Title", required=True)
    summary = fields.Text(string="Summary")
    content = fields.Text(string="Content")
    source_url = fields.Char(string="Source URL")
    date_published = fields.Char(string="Date Published")
    status = fields.Selection([
        ('new', 'New'),
        ('in_review', 'In Review'),
        ('approved', 'Approved'),
        ('archived', 'Archived')
    ], default='new')
