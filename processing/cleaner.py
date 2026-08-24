import pandas as pd
import re

RAW_FILE = "data/raw/topjobs_raw.csv"
CLEANED_FILE = "data/cleaned/topjobs_cleaned.csv"

def clean_ocr_text(text):
    if pd.isna(text):
        return ""
    # Remove unwanted characters, space
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()