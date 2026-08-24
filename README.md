# IT23321854 Job Data Prototype

## Project Overview

**Registration Number:** IT23321854
**Research Component:** Skill Relationship / Technology Stack Analysis
**Data Source:** TopJobs

This prototype establishes a data collection and preprocessing pipeline for IT job advertisements collected from TopJobs. The collected job advertisement data is first stored in a raw CSV format and then processed into a cleaned and standardized schema.

The cleaned dataset will serve as the foundation for future research activities, including semantic skill extraction, skill co occurrence analysis, skill relationship analysis, and technology stack analysis.

## Technical Stack

This project is developed using Python and uses web scraping, OCR, and data processing technologies.

### Web Scraping

• `requests` for fetching web pages and resources
• `beautifulsoup4` for parsing HTML content

### Optical Character Recognition

• `pytesseract` for extracting text from advertisement images
• `Pillow` for loading and processing images

### Data Processing

• `pandas` for data cleaning, deduplication, transformation, and schema formatting

## Project Structure

```text
IT23321854_job_data_prototype/
│
├── scraper/
│   └── topjobs_scraper.py
│
├── processing/
│   └── cleaner.py
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── requirements.txt
├── README.md
└── .venv/
```

## Setup and Execution

### 1. Install Tesseract OCR

Tesseract OCR must be installed on the operating system because TopJobs job advertisements may contain information in image format.

After installation, verify that Tesseract is available from the terminal.

### 2. Create a Python Virtual Environment

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

### 3. Install Python Dependencies

Install the required libraries using:

```bash
pip install -r requirements.txt
```

### 4. Run the Scraper

Execute the TopJobs data collector:

```bash
python scraper/topjobs_scraper.py
```

The scraper collects the available IT job advertisement information and stores the raw results in CSV format.

### 5. Run the Data Cleaner

After collecting the raw data, execute:

```bash
python processing/cleaner.py
```

The cleaner processes the raw dataset by removing duplicates, handling missing values, standardizing fields, and preparing the data for further analysis.

## Data Processing Pipeline

```text
TopJobs
   ↓
Web Scraper
   ↓
Job Advertisement Images
   ↓
OCR using Tesseract
   ↓
Raw CSV Dataset
   ↓
Data Cleaning
   ↓
Standardized CSV Dataset
   ↓
Future Skill Extraction
   ↓
Skill Relationship Analysis
   ↓
Technology Stack Analysis
```

## Challenges and Solutions

### Image Based Job Advertisements

A major challenge identified during prototype development was that some TopJobs job advertisements use images to display important job information rather than providing all information as standard HTML text.

Traditional HTML parsing alone is therefore insufficient for extracting the complete advertisement content.

### OCR Based Solution

To address this limitation, Optical Character Recognition was integrated into the data collection pipeline.

Tesseract OCR is used together with Pillow to process advertisement images and extract the available textual information. The extracted text is then stored as raw data for subsequent processing.

## Current Prototype Limitations

The current OCR output may contain formatting inconsistencies, unnecessary characters, and mixed sections because the text is extracted directly from advertisement images.

The current prototype therefore focuses primarily on establishing the data collection and preprocessing pipeline rather than producing the final research dataset.

## Future Improvements

The cleaner can be extended with regular expressions and additional text processing techniques to identify and separate different sections of job advertisements.

Future improvements include:

• Separating job descriptions and requirements
• Extracting technical skills and technologies
• Normalizing different names for the same technology
• Improving OCR text cleaning
• Removing irrelevant OCR artifacts
• Detecting experience requirements
• Extracting education requirements
• Building skill co occurrence matrices
• Identifying relationships between skills
• Performing technology stack analysis
• Preparing the dataset for future semantic analysis

## Research Contribution

This prototype provides the initial data pipeline required for the **Skill Relationship / Technology Stack Analysis** component of the research project.

The resulting structured dataset can be used in later stages to identify commonly requested technologies, analyze relationships between technical skills, and investigate technology stack patterns within IT job advertisements.

## Author

**Registration Number:** IT23321854
**Research Component:** Skill Relationship / Technology Stack Analysis
**Data Source:** TopJobs
