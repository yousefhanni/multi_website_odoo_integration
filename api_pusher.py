import json
import xmlrpc.client

# Odoo connection 
url = 'http://localhost:8069'
db = 'odoo_test_db'
username = 'admin@example.com'
password = 'admin123'

# Authenticate with Odoo
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common', allow_none=True)
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object', allow_none=True)

# Function to push data to a model
def push_data(model_name, data_list):
    for item in data_list:
        try:
            models.execute_kw(db, uid, password, model_name, 'create', [item])
            print(f"Inserted into {model_name}: {item.get('name') or item.get('title')}")
        except Exception as e:
            print(f"Failed to insert into {model_name}: {e}")

# 1. Push LinkedIn Jobs
with open('linkedin_jobs.json', 'r', encoding='utf-8') as f:
    jobs_data = json.load(f)
    mapped_jobs = [
        {
            "name": job.get('job_title'),
            "company_name": job.get('company_name'),
            "company_logo_url": job.get('company_logo_url'),
            "location": job.get('location'),
            "source_url": job.get('source_url'),
            "date_posted": job.get('date_posted'),
            "status": 'new'
        }
        for job in jobs_data
        if job.get('job_title') and job.get('location')
    ]
    push_data('scraped.job', mapped_jobs)

# 2. Push TechCrunch Blogs
with open('techcrunch_blogs.json', 'r', encoding='utf-8') as f:
    blogs_data = json.load(f)
    mapped_blogs = [
        {
            "title": blog.get('title'),
            "summary": blog.get('summary'),
            "content": blog.get('content'),
            "source_url": blog.get('source_url'),
            "date_published": blog.get('date_published'),
            "status": 'new'
        }
        for blog in blogs_data
        if blog.get('title')
    ]
    push_data('scraped.blog', mapped_blogs)

# 3. Push VentureBeat Page
with open('venturebeat_about.json', 'r', encoding='utf-8') as f:
    page_data = json.load(f)
    mapped_page = {
        "title": page_data.get('page_title'),
        "content": page_data.get('page_content'),
        "source_url": page_data.get('source_url'),
        "status": 'new'
    }
    push_data('scraped.page', [mapped_page])