"""
Google Play Store review scraper.

This script collects customer reviews from Ethiopian banking applications and stores them as raw CSV data.
"""

import hashlib
import logging

import pandas as pd

from google_play_scraper import reviews, Sort

from config.config import (
    APPS,
    RAW_DATA_PATH,
    SCRAPING_LOG_PATH,
    SCRAPE_COUNT
)

# ---------------------------------------------------
# LOGGING CONFIGURATION
# ---------------------------------------------------

logging.basicConfig(
    filename=SCRAPING_LOG_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------------------------------------------
# REVIEW ID GENERATOR
# ---------------------------------------------------

def generate_review_id(review_text, review_date):
    """
    Generate stable hash-based review ID.

    Args:
        review_text (str): review content
        review_date (str): review date

    Returns:
        str: unique hash ID
    """

    unique_string = str(review_text) + str(review_date)

    return hashlib.md5(unique_string.encode()).hexdigest()

# ---------------------------------------------------
# REVIEW SCRAPER
# ---------------------------------------------------

def scrape_reviews_for_app(bank_name, app_id):
    """
    Scrape reviews for a single banking app.

    Args:
        bank_name (str): bank name
        app_id (str): Google Play app ID

    Returns:
        list: collected review dictionaries
    """

    logging.info(f"Starting scrape for {bank_name}")

    try:

        result, continuation_token = reviews(
            app_id,
            lang='en',
            country='et',
            sort=Sort.NEWEST,
            count=SCRAPE_COUNT
        )

        collected_reviews = []

        for review in result:

            review_text = review.get('content')

            review_date = review.get('at')

            review_id = generate_review_id(
                review_text,
                review_date
            )

            collected_reviews.append({
                "review_id": review_id,
                "review": review_text,
                "rating": review.get('score'),
                "date": review_date,
                "bank": bank_name,
                "source": "Google Play"
            })

        logging.info(
            f"Collected {len(collected_reviews)} reviews for {bank_name}"
        )

        return collected_reviews

    except Exception as e:

        logging.error(
            f"Scraping failed for {bank_name}: {e}"
        )

        return []

# ---------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------

def main():
    """
    Main scraping workflow.
    """

    all_reviews = []

    for bank_name, app_id in APPS.items():

        reviews_data = scrape_reviews_for_app(
            bank_name,
            app_id
        )

        all_reviews.extend(reviews_data)

    df = pd.DataFrame(all_reviews)

    try:

        df.to_csv(
            RAW_DATA_PATH,
            index=False
        )

        logging.info(
            f"Raw dataset saved to {RAW_DATA_PATH}"
        )

        print(df.head())

        print(df.shape)

    except Exception as e:

        logging.error(
            f"Failed to save raw dataset: {e}"
        )

# ---------------------------------------------------
# SCRIPT ENTRY POINT
# ---------------------------------------------------

if __name__ == "__main__":
    main()