import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import pytesseract
from PIL import Image
from io import BytesIO
import os

def extract_job_with_ocr(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # fetch the page
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, "html.parser")

        # find the title
        title_element = soup.select_one("h3#position")
        title = title_element.get_text(strip=True) if title_element else ""

        content_element = soup.select_one("#remark")

        extracted_text = ""
        
        if content_element:
            # Check image inside the content container
            image_element = content_element.select_one("img")
            
            if image_element and image_element.has_attr('src'):
                # OCR
                img_url = image_element['src']
                if not img_url.startswith('http'):
                    img_url = "https://www.topjobs.lk" + img_url  # handle relative URLs

                # download the image and perform OCR
                img_response = requests.get(img_url, headers=headers)
                img = Image.open(BytesIO(img_response.content))
                extracted_text = pytesseract.image_to_string(img)
            else:
                # Extract standard text, replacing HTML breaks with newlines
                extracted_text = content_element.get_text(separator="\n", strip=True)

        return {
            "raw_title": title,
            "raw_company": "",
            "raw_description": extracted_text,
            "raw_requirements": "",
            "raw_location": "",
            "raw_posting_date": "",
            "source": "topjobs",
            "url": url,
            "collection_at": datetime.now().strftime("%Y-%m-%d")
        }

    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

if __name__ == "__main__":
    
    job_urls = [
        "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=0&ac=DEFZZZ&jc=0001534246&ec=DEFZZZ&pg=applicant/vacancybyfunctionalarea.jsp",
        "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=1&ac=DEFZZZ&jc=0001534058&ec=DEFZZZ&pg=applicant/vacancybyfunctionalarea.jsp",
        "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=3&ac=0000000223&jc=0001539676&ec=0000000266&pg=applicant/vacancybyfunctionalarea.jsp",
        "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=4&ac=0000000223&jc=0001539674&ec=0000000266&pg=applicant/vacancybyfunctionalarea.jsp",
        "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=5&ac=0000000223&jc=0001539673&ec=0000000266&pg=applicant/vacancybyfunctionalarea.jsp",
        "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=6&ac=0000000201&jc=0001539511&ec=0000000635&pg=applicant/vacancybyfunctionalarea.jsp",
        "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=7&ac=DEFZZZ&jc=0001539191&ec=DEFZZZ&pg=applicant/vacancybyfunctionalarea.jsp",
        "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=8&ac=0000000441&jc=0001539124&ec=0000000583&pg=applicant/vacancybyfunctionalarea.jsp",
        "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=9&ac=DEFZZZ&jc=0001539076&ec=DEFZZZ&pg=applicant/vacancybyfunctionalarea.jsp",
        "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=10&ac=0000000375&jc=0001538862&ec=0000000492&pg=applicant/vacancybyfunctionalarea.jsp"
    ]

    jobs_data = []

    for url in job_urls:
        print(f"Scraping: {url}")
        job = extract_job_with_ocr(url)
        if job:
            jobs_data.append(job)

    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/cleaned", exist_ok=True)

    csv_file = "data/raw/topjobs_raw.csv"
    
    if jobs_data:
        fieldnames = jobs_data[0].keys()
        with open(csv_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(jobs_data)
        
        print(f"\nSuccess! Saved {len(jobs_data)} jobs to {csv_file}")
    else:
        print("\nNo jobs were extracted.")