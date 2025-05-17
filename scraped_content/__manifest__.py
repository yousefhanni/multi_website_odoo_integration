{
    'name': 'Scraped Content Manager',
    'version': '1.0',
    'summary': 'Manage scraped job posts, blogs, and static pages',
    'category': 'Tools',
    'author': 'Youssef Hani',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/scraped_job_views.xml',
        'views/scraped_blog_views.xml',
        'views/scraped_page_views.xml',
    ],
    'installable': True,
    'application': True,
}
