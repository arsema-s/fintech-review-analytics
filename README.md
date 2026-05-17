# Fintech Mobile App Review Analytics

A data engineering and NLP analytics project focused on Ethiopian fintech mobile banking applications. This project collects, preprocesses, analyzes, and visualizes customer reviews from Google Play Store banking apps using transformer-based sentiment analysis and thematic NLP pipelines.

---

# Project Overview

This project analyzes customer feedback from three Ethiopian banking applications:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The workflow includes:

1. Google Play Store review scraping
2. Data cleaning and preprocessing
3. Transformer-based sentiment analysis
4. Thematic analysis using NLP
5. Visualization of customer sentiment and issues
6. Modular NLP pipeline development
7. GitHub version control workflow

---

# Project Structure

```text
fintech-review-analytics/
│
├── config/
│   └── config.py
│
├── logs/
│   ├── scraping.log
│   └── preprocessing.log
│
├── data/
│   └── raw/
│       ├── raw_reviews.csv
│       ├── bank_reviews_cleaned.csv
│       ├── sentiment_reviews.csv
│       └── analyzed_reviews.csv
│
├── notebooks/
│   ├── task1_scraping.ipynb
│   └── task2_sentiment_analysis.ipynb
│
├── reports/
│   └── figures/
│
├── scripts/
│   ├── scrape_reviews.py
│   ├── preprocess_reviews.py
│   └── test_pipeline.py
│
├── src/
│   ├── __init__.py
│   └── nlp_pipeline.py
│
├── .gitignore
├── requirements.txt
└── README.md


Task 1 — Data Collection and Preprocessing
Objective

Collect customer reviews from Google Play Store banking applications and prepare them for NLP analysis.

Technologies Used
Python
pandas
google-play-scraper
Jupyter Notebook
Review Scraping

Reviews were scraped from Google Play Store using the google-play-scraper package.

Banks Included
Bank	Source
CBE	Google Play Store
BOA	Google Play Store
Dashen	Google Play Store
Data Fields Collected
Column	Description
review	Customer review text
rating	App star rating
date	Review submission date
bank	Bank name
source	Review source platform
Preprocessing Steps
- Stable hash-based review ID generation
- Logging for scraping and preprocessing stages
- Separate preprocessing pipeline script
- Centralized configuration management

The following preprocessing operations were performed:

Removal of missing values
Removal of duplicate reviews
Date normalization to YYYY-MM-DD format
Validation of review counts
Dataframe restructuring
CSV export for downstream NLP analysis
Dataset Validation

Each bank contains more than 400 reviews as required by the project guideline.

Validation checks included:

value_counts() verification
isnull() checks
duplicate removal
dataframe shape validation
Output Files
File	Description
raw_reviews.csv	Initial scraped dataset
bank_reviews_cleaned.csv	Cleaned Task 1 dataset
Task 2 — Sentiment and Thematic Analysis
Objective

Perform transformer-based sentiment analysis and identify recurring customer experience themes from banking app reviews.

Technologies Used
transformers
HuggingFace
DistilBERT
spaCy
NLTK
scikit-learn
matplotlib
seaborn
Transformer Model

The following HuggingFace transformer model was used:

distilbert-base-uncased-finetuned-sst-2-english

The model predicts:

POSITIVE sentiment
NEGATIVE sentiment

A custom confidence threshold was used to introduce:

NEUTRAL sentiment
Sentiment Analysis Pipeline

The sentiment workflow included:

Loading cleaned review dataset
Running transformer inference
Extracting sentiment labels
Extracting confidence scores
Creating neutral sentiment class
Saving analyzed dataset
Sentiment Columns Generated
Column	Description
sentiment_label	Predicted review sentiment
sentiment_score	Transformer confidence score
NLP Preprocessing Pipeline

Text preprocessing included:

Lowercasing
URL removal
Special character removal
Tokenization
Lemmatization
Stopword removal

spaCy was used for:

token parsing
lemmatization
linguistic preprocessing
TF-IDF and Keyword Extraction

TF-IDF vectorization was used to identify:

dominant keywords
recurring complaints
frequently discussed app features
customer pain points

Configuration:

TfidfVectorizer(
    max_features=100,
    ngram_range=(1,2)
)
Theme Identification

Reviews were grouped into business-actionable themes.

Themes Included
Theme	Description
Login Issues	Authentication and sign-in failures
OTP Problems	Verification and OTP delivery issues
Transaction Issues	Failed transfers and payments
Performance Issues	Slowdowns, crashes, freezing
UI/UX	Interface and usability feedback
Feature Requests	Suggested improvements
Other	Uncategorized reviews
Modular NLP Pipeline

A reusable NLP module was implemented in:

src/nlp_pipeline.py

The module contains:

clean_text()
identify_theme()

This supports:

reusable preprocessing
modular architecture
scalable NLP workflows
Visualizations

The project includes stakeholder-oriented visualizations such as:

Sentiment distribution by bank
Rating distribution
Theme frequency analysis
Keyword analysis

Visual outputs are stored in:

reports/figures/
Git Workflow

The project uses feature-branch Git workflows.

Branches
Branch	Purpose
main	Stable project branch
task-1	Data collection and preprocessing
task-2	Sentiment and thematic analysis
How to Run the Project
1. Clone Repository
git clone https://github.com/arsema-s/fintech-review-analytics.git
2. Open Project

Open the project folder in VS Code.

3. Create Virtual Environment
py -m venv venv
4. Activate Virtual Environment
Windows
venv\Scripts\activate
5. Install Dependencies
py -m pip install -r requirements.txt
Run Review Scraper
py scripts/scrape_reviews.py
Run NLP Pipeline Test
py -m scripts.test_pipeline
Open Notebooks

Open in Jupyter:

task1_scraping.ipynb
task2_sentiment_analysis.ipynb
Key Insights

Major customer concerns identified include:

login failures
OTP verification problems
transaction failures
application crashes
performance instability

Positive feedback frequently referenced:

ease of transfers
improved interfaces
convenience
accessibility
Future Improvements

Potential future enhancements include:

dashboard deployment
topic modeling with LDA
multilingual Amharic NLP support
real-time review ingestion
PostgreSQL integration
automated reporting pipelines


Author

Arsema Esayas


License

This project is for educational and academic purposes.