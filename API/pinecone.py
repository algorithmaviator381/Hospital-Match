import pinecone
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from data import hospital_dataset,Hospital
from citz_pref import citizen_preferences
from preprocess import preprocess_reviews
from combine_attributes import combine_attributes

pinecone.init(api_key="YOUR_API_KEY")

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
    attribute_vector = combine_attributes(hospital)
    return attribute_vector

# Step 3: Index the hospital data
def index_hospitals(hospital_dataset):
    index = pinecone.Index(index_name="hospital_recommendations")
    
    vectors = []
    for hospital in hospital_dataset:
        attribute_vector = combine_attributes(hospital)
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
    name="User Hospital",
    doctor_speciality="User Speciality",
    cost=500,  # Example cost preference
    people_reviews="",  # Example empty reviews
    icu_facilities=True,  # Example ICU facilities preference
    distance_medicals=10,  # Example distance preference
    distance_hotels=5,  # Example distance preference
    years_of_experience=10,  # Example years of experience preference
    hospital_size="Medium",  # Example hospital size preference
    waiting_time=30,  # Example waiting time preference
    technology_equipment=True,  # Example technology equipment preference
    emergency_response_time="Fast",  # Example emergency response time preference
    specialized_units=["Cardiology", "Orthopedics"],  # Example specialized units preference
    infection_control_measures=True,  # Example infection control measures preference
    accreditation=True,  # Example accreditation preference
    surgical_success_rates=0.9,  # Example surgical success rates preference
    patient_satisfaction=4.5,  # Example patient satisfaction preference
    staff_patient_ratio=0.05,  # Example staff-patient ratio preference
    avg_length_of_stay=5,  # Example average length of stay preference
    availability_specialists=True,  # Example availability of specialists preference
    insurance_coverage=True  # Example insurance coverage preference
)

recommended_hospitals = recommend_hospitals(user_preferences, index)

print(recommended_hospitals)
