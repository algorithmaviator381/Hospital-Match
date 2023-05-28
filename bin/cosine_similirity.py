from sklearn.metrics.pairwise import cosine_similarity

class Hospital:
    def __init__(self, id, name, doctor_speciality, cost, icu_facilities, distance_medicals, distance_hotels, years_of_experience, specialized_units, accreditation, surgical_success_rates, staff_patient_ratio, insurance_coverage):
        self.id = id
        self.name = name
        self.doctor_speciality = doctor_speciality
        self.cost = cost
        self.icu_facilities = icu_facilities
        self.distance_medicals = distance_medicals
        self.distance_hotels = distance_hotels
        self.years_of_experience = years_of_experience
        self.specialized_units = specialized_units
        self.accreditation = accreditation
        self.surgical_success_rates = surgical_success_rates
        self.staff_patient_ratio = staff_patient_ratio
        self.insurance_coverage = insurance_coverage

def create_recommendation(user_preferences, hospitals, top_n=5):
    similarity_scores = []
    for hospital in hospitals:
        hospital_features = [
            hospital.cost,
            hospital.icu_facilities,
            hospital.distance_medicals,
            hospital.distance_hotels,
            hospital.years_of_experience,
            hospital.surgical_success_rates,
            hospital.staff_patient_ratio,
            hospital.insurance_coverage
        ]
        similarity_score = cosine_similarity([user_preferences], [hospital_features])[0][0]
        similarity_scores.append((hospital, similarity_score))

    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    recommendations = similarity_scores[:top_n]
    return recommendations

user_preferences = [3000, True, 2.0, 1.5, 5, 80, 0.6, 90]

hospitals = [
    Hospital(1, "Hospital 1", "Cardiology", 5000, True, 2.5, 1.2, 10, "Cardiac Care Unit", True, 85, 0.5, 90),
    Hospital(2, "Hospital 2", "Orthopedics", 4500, True, 1.8, 0.9, 8, "Orthopedic Surgery", True, 90, 0.6, 80),
    Hospital(3, "Hospital 3", "Neurology", 5500, True, 3.2, 1.5, 12, "Neurological Care Unit", True, 80, 0.4, 95),
    Hospital(4, "Hospital 4", "Oncology", 6000, False, 4.0, 2.0, 15, "Cancer Treatment", False, 70, 0.7, 75),
    Hospital(5, "Hospital 5", "Pediatrics", 4000, True, 2.0, 1.0, 6, "Pediatric Care Unit", True, 95, 0.5, 85),
    Hospital(6, "Hospital 6", "Dermatology", 3500, False, 2.5, 1.2, 8, "Dermatology Clinic", True, 70, 0.6, 70),
    Hospital(7, "Hospital 7", "Gynecology", 4800, True, 3.5, 1.7, 10, "Maternity Care Unit", True, 75, 0.4, 90),
    Hospital(8, "Hospital 8", "Urology", 4200, False, 2.8, 1.4, 9, "Urology Clinic", True, 80, 0.5, 80),
    Hospital(9, "Hospital 9", "ENT", 3800, True, 1.5, 0.8, 7, "ENT Clinic", False, 65, 0.8, 70),
    Hospital(10, "Hospital 10", "Psychiatry", 4400, True, 2.2, 1.1, 6, "Psychiatric Care Unit", True, 90, 0.6, 85)
]

recommendations = create_recommendation(user_preferences, hospitals, top_n=3)

for hospital, similarity_score in recommendations:
    print(f"Recommended Hospital: {hospital.name} | Similarity Score: {similarity_score}")
