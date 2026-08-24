Project Overview
Registration Number: IT23321854

Research Component: Skill Relationship / Technology Stack Analysis

Data Source: TopJobs

Objective: This prototype establishes a data collection pipeline to scrape IT job advertisements. The collected data is saved in a raw CSV format and then processed into a cleaned, common schema to prepare for future semantic skill extraction, co-occurrence matrices, and technology stack analysis.

Technical Stack
This project relies on Python and requires both web scraping and image processing tools.

Web Scraping: requests for fetching pages, beautifulsoup4 for HTML parsing.

Image Processing (OCR): pytesseract and Pillow for reading text from images.

Data Processing: pandas for cleaning, deduplication, and schema formatting.

Setup & Execution
Follow these steps to run the pipeline:

Install the Tesseract OCR software on your operating system.

Create and activate a Python virtual environment (python -m venv .venv).

Install the required Python libraries using pip install -r requirements.txt.

Execute the data collector by running python scraper/topjobs_scraper.py.

Clean and format the dataset by running python processing/cleaner.py.

Challenges & Solutions
During the prototype development, a major technical hurdle was identified regarding how data is rendered on the target website.

Challenge: TopJobs uses image-based job advertisements instead of standard HTML text, making traditional DOM parsing ineffective.

Solution: Implemented Optical Character Recognition (OCR) using Tesseract and Pillow to extract raw text directly from the advertisement images.

Future Improvement: Implement regular expressions (Regex) in the cleaner script to accurately separate the raw OCR text into distinct "Requirements" and "Description" columns for the final schema.