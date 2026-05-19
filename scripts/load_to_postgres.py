import os
import hashlib
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv


# LOAD ENVIRONMENT VARIABLES

load_dotenv()

USERNAME = os.getenv("DB_USERNAME")

PASSWORD = os.getenv("DB_PASSWORD")

HOST = os.getenv("DB_HOST")

PORT = os.getenv("DB_PORT")

DATABASE = os.getenv("DB_NAME")


# DATABASE CONNECTION

engine = create_engine(
    f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
)


# LOAD DATASET

df = pd.read_csv(
    "data/raw/analyzed_reviews.csv"
)


# GENERATE UNIQUE REVIEW IDS

def generate_review_id(review_text, review_date, row_index):

    unique_string = (
        str(review_text)
        + str(review_date)
        + str(row_index)
    )

    return hashlib.md5(
        unique_string.encode()
    ).hexdigest()

df["review_id"] = df.apply(
    lambda row: generate_review_id(
        row["review"],
        row["date"],
        row.name
    ),
    axis=1
)



# CREATE BANK TABLE

banks_df = pd.DataFrame({
    "bank_name": df["bank"].unique()
})


# CHECK EXISTING BANKS

existing_banks = pd.read_sql(
    "SELECT bank_name FROM banks",
    engine
)

existing_bank_names = existing_banks["bank_name"].tolist()


# FILTER NEW BANKS ONLY

new_banks_df = banks_df[
    ~banks_df["bank_name"].isin(existing_bank_names)
]


# INSERT ONLY NEW BANKS

if not new_banks_df.empty:

    new_banks_df.to_sql(
        "banks",
        engine,
        if_exists="append",
        index=False
    )

    print("New banks inserted.")

else:

    print("Banks already exist. Skipping insertion.")


# FETCH BANK IDS

bank_lookup = pd.read_sql(
    "SELECT * FROM banks",
    engine
)

df = df.merge(
    bank_lookup,
    left_on="bank",
    right_on="bank_name"
)


# CREATE REVIEWS TABLE

reviews_df = df[[
    "review_id",
    "bank_id",
    "review",
    "rating",
    "date",
    "source"
]]

reviews_df = reviews_df.rename(
    columns={
        "date": "review_date"
    }
)

reviews_df.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)


# CREATE SENTIMENTS TABLE

sentiment_df = df[[
    "review_id",
    "sentiment_label",
    "sentiment_score",
    "identified_theme"
]]

sentiment_df = sentiment_df.rename(
    columns={
        "identified_theme": "theme"
    }
)

sentiment_df.to_sql(
    "sentiments",
    engine,
    if_exists="append",
    index=False
)

print("Data successfully loaded into PostgreSQL.")