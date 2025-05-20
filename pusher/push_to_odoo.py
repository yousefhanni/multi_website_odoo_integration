import os
import json
import logging
import xmlrpc.client
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_fixed

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load .env variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
url = os.getenv("ODOO_URL") 
db = os.getenv("ODOO_DB")
username = os.getenv("ODOO_USER")
password = os.getenv("ODOO_PASSWORD")

# Odoo XML-RPC setup
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common", allow_none=True)
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object", allow_none=True)

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def create_if_not_exists(model_name, domain, values):
    existing = models.execute_kw(db, uid, password, model_name, 'search_read', [domain], {'limit': 1})
    if existing:
        logging.info(f"Skipped (already exists): {values.get('title') or values.get('name')}")
        return
    models.execute_kw(db, uid, password, model_name, 'create', [values])
    logging.info(f"Inserted into {model_name}: {values.get('title') or values.get('name')}")

def push_jobs():
    with open('linkedin_jobs.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for job in data:
            values = {
                "name": job.get("job_title"),
                "company_name": job.get("company_name"),
                "company_logo_url": job.get("company_logo_url"),
                "location": job.get("location"),
                "source_url": job.get("source_url"),
                "date_posted": job.get("date_posted"),
                "status": "new"
            }
            if values["name"] and values["company_name"]:
                create_if_not_exists("scraped.job", [["name", "=", values["name"]], ["company_name", "=", values["company_name"]]], values)

def push_blogs():
    with open('techcrunch_blogs.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for blog in data:
            values = {
                "title": blog.get("title"),
                "summary": blog.get("summary"),
                "content": blog.get("content"),
                "source_url": blog.get("source_url"),
                "date_published": blog.get("date_published"),
                "status": "new"
            }
            if values["title"]:
                create_if_not_exists("scraped.blog", [["title", "=", values["title"]]], values)

                # Push to website.blog.post
                website_post = {
                    "name": values["title"],
                    "content": values["content"]
                }
                create_if_not_exists("blog.post", [["name", "=", website_post["name"]]], website_post)


def push_page():
    with open('venturebeat_about.json', 'r', encoding='utf-8') as f:
        page = json.load(f)
        values = {
            "title": page.get("page_title"),
            "content": page.get("page_content"),
            "source_url": page.get("source_url"),
            "status": "new"
        }
        if values["title"]:
            create_if_not_exists("scraped.page", [["title", "=", values["title"]]], values)

            # Push to website.page
            website_page = {
                "name": values["title"],
                "url": f"/{values['title'].lower().replace(' ', '-')}",
                "website_published": True,
                "type": "qweb",
                "arch": f"<t t-name='{values['title'].lower().replace(' ', '_')}'><div>{values['content']}</div></t>"
            }
            create_if_not_exists("website.page", [["name", "=", website_page["name"]]], website_page)

if __name__ == "__main__":
    push_jobs()
    push_blogs()
    push_page()