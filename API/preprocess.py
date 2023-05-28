import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#This code snippet is for patients reviews, not needed in current code

def preprocess_reviews(reviews):
    nltk.download('stopwords')
    nltk.download('punkt')
    
    preprocessed_reviews = []
    stop_words = set(stopwords.words('english'))

    for review in reviews:
        review = review.lower()
        review = re.sub(r'[^a-zA-Z]', ' ', review)
        tokens = word_tokenize(review)
        
        filtered_tokens = [token for token in tokens if token not in stop_words]
        
        preprocessed_review = ' '.join(filtered_tokens)
        
        preprocessed_reviews.append(preprocessed_review)
    
    return preprocessed_reviews
