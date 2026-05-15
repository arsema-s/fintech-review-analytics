from google_play_scraper import reviews, Sort
import pandas as pd

# CBE: com.combanketh.mobilebanking
# BOA: com.boa.boaMobileBanking
# Dashen: com.dashen.dashensuperapp

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank_name, app_id in apps.items():

    print(f"Scraping reviews for {bank_name}...")

    result, continuation_token = reviews(
        app_id,
        lang='en',
        country='et',
        sort=Sort.NEWEST,
        count=500
    )

    for review in result:

        all_reviews.append({
            "review": review['content'],
            "rating": review['score'],
            "date": review['at'],
            "bank": bank_name,
            "source": "Google Play"
        })

    print(f"Collected {len(result)} reviews for {bank_name}")

    df = pd.DataFrame(all_reviews)

    print(df.head())
    print(df.shape)

    df.to_csv("data/raw/raw_reviews.csv", index=False)