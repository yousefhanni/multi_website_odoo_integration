# 🛠 Multi-Website Odoo Integration

This project integrates web-scraped content into an Odoo module via API. It includes:
- Web Scraping Scripts (LinkedIn, TechCrunch, VentureBeat)
- A custom Odoo module (scraped_content)
- An API pusher script
- Structured JSON outputs
- Instructions for setup and use

---

## 📁 Project Structure

```
multi_website_odoo_integration/
├── api_pusher.py
├── data/
│   ├── linkedin_jobs.json
│   ├── techcrunch_blogs.json
│   └── venturebeat_about.json
├── scraping_scripts/
│   ├── scrape_linkedin.py
│   ├── scrape_techcrunch.py
│   ├── scrape_venturebeat_about.py
│   └── chromedriver.exe
├── scraped_content/
│   ├── __manifest__.py
│   ├── __init__.py
│   ├── models/
│   ├── views/
│   └── security/
└── screenshots/
    ├── jobs_linkedin_in_odoo.png
    ├── blogs_techcrunch_in_odoo.png
    ├── page_venturebeat_in_odoo.png
    ├── job_form_detail.png
    └── blog_form_detail.png
```

---

## ✅ Setup Instructions

### 🔧 Python Dependencies

```bash
pip install selenium beautifulsoup4 requests
```

### 🧰 ChromeDriver

1. Check your Chrome version from `chrome://settings/help`
2. Download the matching version from: https://googlechromelabs.github.io/chrome-for-testing/
3. Place `chromedriver.exe` inside the `scraping_scripts/` folder

---

## ▶️ How to Run the Scraper Scripts

Navigate to the `scraping_scripts/` folder and run:

```bash
python scrape_linkedin.py
python scrape_techcrunch.py
python scrape_venturebeat_about.py
```

Each script will generate its corresponding `.json` file inside the `data/` folder.

---

## 📤 How to Push Data to Odoo

1. Make sure Odoo is running and the `scraped_content` module is installed.
2. Update `api_pusher.py` with correct login credentials and file paths if necessary.
3. Run the script:

```bash
python api_pusher.py
```

The script will:
- Authenticate using XML-RPC
- Push data to Odoo using `scraped.job`, `scraped.blog`, and `scraped.page` models

---

## 🧩 How to Install & Use the Odoo Module

1. Copy the `scraped_content/` folder into your Odoo custom addons path.
2. Update your `odoo.conf` if needed:

```ini
addons_path = /path/to/odoo/addons,/path/to/your/custom/modules
```

3. Restart the Odoo server:

```bash
python odoo-bin -c odoo.conf
```

4. Activate Developer Mode in Odoo.
5. Go to **Apps** → Click **Update Apps List**
6. Search for `Scraped Content` and click **Install**

7. After installation, you’ll see a new menu:

**Scraping Manager** → Jobs / Blogs / Pages

---

## 📸 Screenshots – Output

### ✅ Jobs List in Odoo  
![Jobs List](./screenshots/jobs_linkedin_in_odoo.png)

### ✅ Job Detail View  
![Job Detail](./screenshots/job_form_detail.png)

### ✅ Blog List View  
![Blog List](./screenshots/blogs_techcrunch_in_odoo.png)

### ✅ Blog Detail View  
![Blog Detail](./screenshots/blog_form_detail.png)

### ✅ VentureBeat Page Content  
![Page Detail](./screenshots/page_venturebeat_in_odoo.png)
