import pinecone
from data import hospital_dataset
from hospital_vector_database import index_name

index = pinecone.Index(index_name=index_name)

def recommend_hospitals(query_vector, top_k=5, preferences=None):
        response = index.query(queries=query_vector, top_k=top_k)

        # Filter and sort the recommended hospitals based on user preferences
        if preferences:
            response_ids = response.ids
            filtered_ids = []
            for hospital_id in response_ids:
                hospital = hospital_dataset[int(hospital_id) - 1]  # Assuming hospital ids start from 1
                if preferences["doctor_speciality"] in hospital.doctor_speciality and \
                        hospital.cost <= preferences["max_cost"] and \
                        hospital.icu_facilities == preferences["icu_facilities"] and \
                        hospital.years_of_experience >= preferences["min_experience"]:
                    filtered_ids.append(hospital_id)
            
            response_ids = filtered_ids

            # Sort the filtered hospital ids based on a criterion (e.g., patient satisfaction)
            response_ids = sorted(response_ids, key=lambda x: hospital_dataset[int(x) - 1].patient_satisfaction, reverse=True)

        else:
            response_ids = response.ids

        return response_ids