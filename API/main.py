import numpy as np
from citz_pref import collect_citizen_preferences
from data import hospital_dataset
from recommendations import recommend_hospitals
from hospital_vector_database import index, embeddings, index_name, delete_index

def main():

    for hospital in hospital_dataset:
        vector = np.random.rand(100)
        embeddings.append(vector)
        index.upsert(item_id=str(hospital.id), data=vector)

    query_vector = np.random.rand(100)
    preferences = collect_citizen_preferences()

    recommended_hospitals = recommend_hospitals(query_vector, top_k=3, preferences=preferences)
    
    for hospital_id in recommended_hospitals:
        hospital = hospital_dataset[int(hospital_id) - 1]
        print("Hospital ID:", hospital.id)
        print("Hospital Name:", hospital.name)
        print("Doctor Speciality:", hospital.doctor_speciality)

    delete_index()

if __name__ == '__main__':
    main()
