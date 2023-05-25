import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_reviews(reviews):
    # Initialize NLTK resources
    nltk.download('stopwords')
    nltk.download('punkt')
    
    # Preprocessing steps
    preprocessed_reviews = []
    stop_words = set(stopwords.words('english'))

    for review in reviews:
        # Convert to lowercase
        review = review.lower()
        
        # Remove special characters and numbers
        review = re.sub(r'[^a-zA-Z]', ' ', review)
        
        # Tokenization
        tokens = word_tokenize(review)
        
        # Remove stopwords
        filtered_tokens = [token for token in tokens if token not in stop_words]
        
        # Join the tokens back into a sentence
        preprocessed_review = ' '.join(filtered_tokens)
        
        preprocessed_reviews.append(preprocessed_review)
    
    return preprocessed_reviews
