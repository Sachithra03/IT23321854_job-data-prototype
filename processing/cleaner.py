import pandas as pd
import re
import os

RAW_FILE = "data/raw/topjobs_raw.csv"
CLEANED_FILE = "data/cleaned/topjobs_cleaned.csv"

def clean_ocr_text(text):
    if pd.isna(text):
        return ""

    text = str(text)
    # Remove unwanted newlines, space
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)

    return text.strip()

def process_data():
    print(f"Reading raw data from {RAW_FILE}...")
    df = pd.read_csv(RAW_FILE)

    cleaned = pd.DataFrame()

    # generate unique job_id for each job
    cleaned['job_id'] = [f"topjobs_{i:03d}" for i in range(1, len(df) + 1)]

    # Static and straightforward mapping
    cleaned['source'] = df["source"]
    cleaned['country'] = "Sri Lanka"
    cleaned['job_title'] = df["raw_title"]

    # Clean the OCR text
    cleaned['company_name'] = df["raw_company"].fillna("")
    cleaned['description'] = df["raw_description"].apply(clean_ocr_text)
    cleaned['requirements'] = df["raw_requirements"].apply(clean_ocr_text)
    cleaned['location'] = df["raw_location"].fillna("")

    # dates and urls
    cleaned['posting_date'] = df["raw_posting_date"].fillna("")
    cleaned['url'] = df["url"]

    #collected_at column matches - scraper output
    if 'collection_at' in df.columns:
        cleaned['collected_at'] = df["collection_at"]
    else:
        cleaned['collected_at'] = ""

    # Duplication
    initial_count = len(cleaned)
    cleaned = cleaned.drop_duplicates(subset=["url"], keep="first")
    final_count = len(cleaned)

    if initial_count - final_count > 0:
        print(f"Removed {initial_count - final_count} duplicate records.")

    # Save the final dataset
    os.makedirs("data/cleaned", exist_ok=True)
    cleaned.to_csv(CLEANED_FILE, index=False, encoding='utf-8')

    print(f"Success! Saved {len(cleaned)} cleaned records to {CLEANED_FILE}.")
    print("Schema Columns:", cleaned.columns.tolist())

if __name__ == "__main__":
    process_data()


