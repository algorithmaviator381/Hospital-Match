import pinecone
import numpy as np
from citz_pref import collect_citizen_preferences

class Hospital:
    def __init__(self, id, name, doctor_speciality, phone, cost, icu_facilities, years_of_experience, specialized_units, infection_control_measures, accreditation, surgical_success_rates, patient_satisfaction, insurance_coverage, beds_availability):
        self.id = id
        self.name = name
        self.doctor_speciality = doctor_speciality
        self.phone = phone
        self.cost = cost
        self.icu_facilities = icu_facilities
        self.years_of_experience = years_of_experience
        self.specialized_units = specialized_units
        self.infection_control_measures = infection_control_measures
        self.accreditation = accreditation
        self.surgical_success_rates = surgical_success_rates
        self.patient_satisfaction = patient_satisfaction
        self.insurance_coverage = insurance_coverage
        self.beds_availability = beds_availability

from data import hospital_dataset

def main():
    pinecone.init(api_key="A_P_I_K_E_Y")
    index_name = "hospital-recommendation"
    pinecone.create_index(name=index_name, dimension=100, metric="cosine")

    index = pinecone.Index(index_name=index_name)
    embeddings = []

    for hospital in hospital_dataset:
        vector = np.random.rand(100)  # Replace this with your actual vector representation of each hospital
        embeddings.append(vector)
        index.upsert(item_id=str(hospital.id), data=vector)

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

    # Example usage:
    query_vector = np.random.rand(100)  # Replace this with your actual query vector

    # User preferences (modify as per your requirements)
    preferences = collect_citizen_preferences()

    recommended_hospitals = recommend_hospitals(query_vector, top_k=5, preferences=preferences)
    for hospital_id in recommended_hospitals:
        hospital = hospital_dataset[int(hospital_id) - 1]
        print("Hospital ID:", hospital.id)
        print("Hospital Name:", hospital.name)
        print("Doctor Speciality:", hospital.doctor_speciality)
        # Add more attributes to display as per your requirement

    pinecone.delete_index(index_name=index_name)
    pinecone.deinit()

if __name__ == '__main__':
    main()
