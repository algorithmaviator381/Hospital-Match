import pinecone
import numpy as np
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from data import hospital_dataset,Hospital
#from citz_pref import citizen_preferences  #importing citizen preferences  
from preprocess import preprocess_reviews
from combine_attributes import attributes_array

pinecone.init(api_key="API_KEY!!!!")

# Step 1: Preprocess and vectorize reviews (module preprocess)
def preprocess_reviews(reviews):
    preprocessed_reviews = preprocess_reviews(reviews)
    return preprocessed_reviews

def vectorize_reviews(preprocessed_reviews):
    vectorizer = TfidfVectorizer()  #vectorization technique
    review_vectors = vectorizer.fit_transform(preprocessed_reviews).toarray()
    return review_vectors

# Step 2: Combine attribute vectors (module combine_attributes)
def combine_attributes(hospital):
    attribute_vector = attributes_array(hospital)
    return attribute_vector

# Step 3: Index the hospital data
def index_hospitals(hospital_dataset):
    index = pinecone.Index(index_name="hospital_recommendations")
    
    vectors = []
    for hospital in hospital_dataset:
        attribute_vector = attributes_array(hospital)
        vectors.append(attribute_vector)

    # Convert review text into vectors
    preprocessed_reviews = preprocess_reviews([hospital.people_reviews for hospital in hospital_dataset])
    review_vectors = vectorize_reviews(preprocessed_reviews)

    # Concatenate attribute vectors with review vectors
    concatenated_vectors = np.concatenate((vectors, review_vectors), axis=1)

    # Index the hospital vectors
    index.upsert(items=np.array(concatenated_vectors), ids=np.array([hospital.name for hospital in hospital_dataset]))

    return index

# Step 4: Rank hospitals based on user preferences
def recommend_hospitals(user_preferences, index, num_results=10):
    # Convert user preferences into a query vector
    user_vector = combine_attributes(user_preferences)
    user_vector = np.concatenate((user_vector, np.zeros_like(user_vector)))  # Pad with zeros for review vectors

    # Search the index to retrieve similar hospitals
    _, results = index.query(queries=[user_vector], top_k=num_results)

    return results[0].ids  # Return the IDs of the recommended hospitals

# Step 3: Index the hospital data
index = index_hospitals(hospital_dataset)

# Step 4: Rank hospitals based on user preferences
user_preferences = Hospital(
    id="1",
    name="User Hospital",
    doctor_speciality="User Speciality",
    cost=500,
    people_reviews="",  #NULL reviews
    icu_facilities=True, 
    distance_medicals=10,
    distance_hotels=5,  
    years_of_experience=10,
    hospital_size="Medium",
    waiting_time=30,  
    technology_equipment=True,  
    emergency_response_time="Fast",
    specialized_units=["Cardiology", "Orthopedics"],  
    infection_control_measures=True,  
    accreditation=True,  
    surgical_success_rates=0.9,
    patient_satisfaction=4.5,  
    staff_patient_ratio=0.05,  
    avg_length_of_stay=5,  
    availability_specialists=True, 
    insurance_coverage=True  
)

recommended_hospitals = recommend_hospitals(user_preferences, index)
print(recommended_hospitals)