"""
Centralized project configuration.
"""

APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

RAW_DATA_PATH = "data/raw/raw_reviews.csv"

CLEAN_DATA_PATH = "data/raw/bank_reviews_cleaned.csv"

SCRAPING_LOG_PATH = "logs/scraping.log"

PREPROCESS_LOG_PATH = "logs/preprocessing.log"

SCRAPE_COUNT = 1000