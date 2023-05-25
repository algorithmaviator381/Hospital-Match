import pinecone
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from data import hospital_dataset
from citz_pref import citizen_preferences
from preprocess import preprocess_reviews
from combine_attributes import combine_attributes

# Step 1: Preprocess and vectorize reviews (module preprocess)
def preprocess_reviews(reviews):
    preprocessed_reviews = preprocess_reviews(reviews)
    return preprocessed_reviews

def vectorize_reviews(preprocessed_reviews):
    vectorizer = TfidfVectorizer()  #vectorization technique
    review_vectors = vectorizer.fit_transform(preprocessed_reviews).toarray()
    return review_vectors

# Step 2: Combine attribute vectors (module combine_attributes)
def combine_attributes(hospital_dataset):
    attribute_vector = combine_attributes(hospital_dataset)
    return attribute_vector


# Step 3: Index the hospital data
def index_hospitals(hospitals):
    pinecone.init(api_key="YOUR_API_KEY")  # Initialize Pinecone with your API key
    index = pinecone.Index(index_name="hospital_recommendations")

    vectors = []
    for hospital in hospitals:
        attribute_vector = combine_attributes(hospital)
        vectors.append(attribute_vector)

    # Convert review text into vectors
    preprocessed_reviews = preprocess_reviews([hospital.people_reviews for hospital in hospitals])
    review_vectors = vectorize_reviews(preprocessed_reviews)

    # Concatenate attribute vectors with review vectors
    concatenated_vectors = np.concatenate((vectors, review_vectors), axis=1)

    # Index the hospital vectors
    index.upsert(items=np.array(concatenated_vectors), ids=np.array([hospital.name for hospital in hospitals]))

    return index

# Step 4: Rank hospitals based on user preferences
def recommend_hospitals(user_preferences, index, num_results=10):
    # Convert user preferences into a query vector
    user_vector = combine_attributes(user_preferences)
    user_vector = np.concatenate((user_vector, np.zeros_like(user_vector)))  # Pad with zeros for review vectors

    # Search the index to retrieve similar hospitals
    _, results = index.query(queries=[user_vector], top_k=num_results)

    return results[0].ids  # Return the IDs of the recommended hospitals

# Example usage
hospitals = [...]  # List of Hospital objects

# Step 3: Index the hospital data
index = index_hospitals(hospitals)

# Step 4: Rank hospitals based on user preferences
#user_preferences = Hospital(...)  # User preferences
# recommended_hospitals = recommend_hospitals(user_preferences, index)

# print(recommended_hospitals)
