import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    return response.text


def scrape_job(url):
    html = get_page(url)
    soup = BeautifulSoup(html, "html.parser")

    title = ""
    company = ""
    description = ""
    requirements = ""
    location = ""
    posting_date = ""

    title_tag = soup.select_one("col-xs-8 job-title")

    if title_tag:
        title = title_tag.get_text(" ", strip=True)

    company_tag = soup.select_one("YOUR_COMPANY_SELECTOR")

    if company_tag:
        company = company_tag.get_text(" ", strip=True)

    return {
        "title": title,
        "company": company,
        "description": description,
        "requirements": requirements,
        "location": location,
        "posting_date": posting_date,
        "source": "topjobs",
        "url": url,
        "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    test_url = "https://www.topjobs.lk/"

    job = scrape_job(test_url)

    for key, value in job.items():
        print(f"{key}: {value}")