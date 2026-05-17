from src.nlp_pipeline import clean_text
from src.nlp_pipeline import identify_theme

sample_review = """
The app crashes during transfers and login fails constantly.
"""

cleaned = clean_text(sample_review)

theme = identify_theme(cleaned)

print("CLEANED TEXT:")
print(cleaned)

print("\nIDENTIFIED THEME:")
print(theme)