import re
import nltk
import spacy
from nltk.corpus import stopwords

nltk.download('stopwords')
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words('english'))

def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    doc = nlp(text)

    cleaned_tokens = []

    for token in doc:

        lemma = token.lemma_

        if (
            lemma not in stop_words
            and len(lemma) > 2
        ):

            cleaned_tokens.append(lemma)

    return " ".join(cleaned_tokens)

def identify_theme(text):

    text = text.lower()

    if any(word in text for word in [
        'login',
        'password',
        'signin',
        'authenticate'
    ]):
        return 'Login Issues'

    elif any(word in text for word in [
        'otp',
        'verification',
        'code'
    ]):
        return 'OTP Problems'

    elif any(word in text for word in [
        'transfer',
        'transaction',
        'send',
        'payment'
    ]):
        return 'Transaction Issues'

    elif any(word in text for word in [
        'crash',
        'slow',
        'lag',
        'freeze'
    ]):
        return 'Performance Issues'

    elif any(word in text for word in [
        'ui',
        'design',
        'interface',
        'layout'
    ]):
        return 'UI/UX'

    elif any(word in text for word in [
        'fingerprint',
        'feature',
        'update'
    ]):
        return 'Feature Requests'

    else:
        return 'Other'

