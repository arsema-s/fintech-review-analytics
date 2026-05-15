"""
Review preprocessing pipeline.

This script:
- removes duplicates,
- removes missing values,
- normalizes dates,
- exports cleaned dataset.
"""

import logging

import pandas as pd

from config.config import (
    RAW_DATA_PATH,
    CLEAN_DATA_PATH,
    PREPROCESS_LOG_PATH
)

# ---------------------------------------------------
# LOGGING CONFIGURATION
# ---------------------------------------------------

logging.basicConfig(
    filename=PREPROCESS_LOG_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ---------------------------------------------------
# DATA PREPROCESSING
# ---------------------------------------------------

def preprocess_reviews():
    """
    Clean raw review dataset.

    Returns:
        pandas.DataFrame: cleaned dataset
    """

    try:

        logging.info("Loading raw dataset")

        df = pd.read_csv(RAW_DATA_PATH)

        logging.info(
            f"Initial dataset shape: {df.shape}"
        )

    except Exception as e:

        logging.error(
            f"Failed to load dataset: {e}"
        )

        raise

    # ---------------------------------------------
    # REMOVE DUPLICATES
    # ---------------------------------------------

    before_duplicates = df.shape[0]

    df = df.drop_duplicates(
        subset=['review_id']
    )

    after_duplicates = df.shape[0]

    logging.info(
        f"Removed {before_duplicates - after_duplicates} duplicate rows"
    )

    # ---------------------------------------------
    # REMOVE MISSING VALUES
    # ---------------------------------------------

    before_missing = df.shape[0]

    df = df.dropna(
        subset=['review', 'rating']
    )

    after_missing = df.shape[0]

    logging.info(
        f"Removed {before_missing - after_missing} rows with missing values"
    )

    # ---------------------------------------------
    # NORMALIZE DATES
    # ---------------------------------------------

    df['date'] = pd.to_datetime(
        df['date']
    ).dt.strftime('%Y-%m-%d')

    logging.info("Normalized date format")

    # ---------------------------------------------
    # SAVE CLEAN DATASET
    # ---------------------------------------------

    try:

        df.to_csv(
            CLEAN_DATA_PATH,
            index=False
        )

        logging.info(
            f"Clean dataset saved to {CLEAN_DATA_PATH}"
        )

    except Exception as e:

        logging.error(
            f"Failed to save clean dataset: {e}"
        )

        raise

    return df

# ---------------------------------------------------
# SCRIPT ENTRY POINT
# ---------------------------------------------------

if __name__ == "__main__":

    cleaned_df = preprocess_reviews()

    print(cleaned_df.head())

    print(cleaned_df.shape)