from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?keywords=python%20developer&location=Egypt")

time.sleep(5)

jobs = driver.find_elements(By.CLASS_NAME, 'base-card')
job_list = []

for job in jobs:
    try:
        title = job.find_element(By.CLASS_NAME, 'base-search-card__title').text.strip()
        company = job.find_element(By.CLASS_NAME, 'base-search-card__subtitle').text.strip()
        location = job.find_element(By.CLASS_NAME, 'job-search-card__location').text.strip()
        link = job.find_element(By.TAG_NAME, 'a').get_attribute('href')

        try:
            logo_url = job.find_element(By.CLASS_NAME, 'artdeco-entity-image').get_attribute('src')
        except:
            logo_url = None

        try:
            date_posted = job.find_element(By.CLASS_NAME, 'job-search-card__listdate').text.strip()
        except:
            try:
                date_posted = job.find_element(By.TAG_NAME, 'time').text.strip()
            except:
                date_posted = None

        job_list.append({
            "job_title": title,
            "company_name": company,
            "company_logo_url": logo_url,
            "location": location,
            "source_url": link,
            "date_posted": date_posted
        })

    except Exception as e:
        print("Error:", e)


with open("linkedin_jobs.json", "w", encoding="utf-8") as f:
    json.dump(job_list, f, ensure_ascii=False, indent=2)

print("Data is Saved in linkedin_jobs.json")
driver.quit()
