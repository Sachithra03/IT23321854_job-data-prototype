import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import pytesseract
from PIL import Image
from io import BytesIO

def extract_job_with_ocr(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        #fetch the page
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, "html.parser")

        #find the title and image url
        title_element = soup.select_one("h3#position")
        title = title_element.get_text(strip=True) if title_element else ""

        #find the image url
        image_element = soup.select_one("#remark img")

        ocr_text = ""
        if image_element and image_element.has_attr('src'):
            img_url = image_element['src']
            if not img_url.startswith('http'):
                img_url = "https://www.topjobs.lk" + img_url  #handle relative URLs

            #download the image and perform OCR
            img_response = requests.get(img_url, headers=headers)
            img = Image.open(BytesIO(img_response.content))
            ocr_text = pytesseract.image_to_string(img)

        return {
            "raw_title": title,
            "raw_company": "",
            "raw_description": ocr_text,
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
    test_url = "https://www.topjobs.lk/employer/JobAdvertismentServlet?rid=8&ac=0000000441&jc=0001539124&ec=0000000583&pg=applicant/vacancybyfunctionalarea.jsp"
    job = extract_job_with_ocr(test_url)
    if job:
        print("Extracted Text from Image:\n", job['raw_description'][:500]) # Print first 500