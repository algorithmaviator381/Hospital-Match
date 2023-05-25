import pinecone
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from data import hospital_dataset
from citz_pref import citizen_preferences
from preprocess import preprocess_reviews

# Step 1: Preprocess and vectorize reviews
def preprocess_reviews(reviews):
    preprocessed_reviews = preprocess_reviews(reviews)
    return preprocessed_reviews

def vectorize_reviews(preprocessed_reviews):
    vectorizer = TfidfVectorizer()  #vectorization technique
    review_vectors = vectorizer.fit_transform(preprocessed_reviews).toarray()
    return review_vectors

# Step 2: Combine attribute vectors
def combine_attributes(hospital):
    attribute_vector = np.array([
        hospital.cost,
        hospital.available_beds,
        hospital.staff_quality,
        hospital.icu_facilities,
        hospital.distance_medicals,
        hospital.distance_hotels,
        hospital.years_of_experience,
        hospital.hospital_size,
        hospital.waiting_time,
        hospital.technology_equipment,
        hospital.emergency_response_time,
        hospital.specialized_units,
        hospital.infection_control_measures,
        hospital.accreditation,
        hospital.surgical_success_rates,
        hospital.patient_satisfaction,
        hospital.staff_patient_ratio,
        hospital.avg_length_of_stay,
        hospital.availability_specialists,
        hospital.insurance_coverage
    ])    
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
