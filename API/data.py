class Hospital:
    def __init__(self, name, doctor_speciality, cost, people_reviews, icu_facilities, distance_medicals, distance_hotels, years_of_experience, hospital_size, waiting_time, technology_equipment, emergency_response_time, specialized_units, infection_control_measures, accreditation, surgical_success_rates, patient_satisfaction, staff_patient_ratio, avg_length_of_stay, availability_specialists, insurance_coverage):
        self.name = name
        self.doctor_speciality = doctor_speciality
        self.cost = cost
        self.people_reviews = people_reviews
        self.icu_facilities = icu_facilities
        self.distance_medicals = distance_medicals
        self.distance_hotels = distance_hotels
        self.years_of_experience = years_of_experience
        self.hospital_size = hospital_size
        self.waiting_time = waiting_time
        self.technology_equipment = technology_equipment
        self.emergency_response_time = emergency_response_time
        self.specialized_units = specialized_units
        self.infection_control_measures = infection_control_measures
        self.accreditation = accreditation
        self.surgical_success_rates = surgical_success_rates
        self.patient_satisfaction = patient_satisfaction
        self.staff_patient_ratio = staff_patient_ratio
        self.avg_length_of_stay = avg_length_of_stay
        self.availability_specialists = availability_specialists
        self.insurance_coverage = insurance_coverage

hospital_dataset = [
    Hospital(
        name="Hospital A",
        doctor_speciality="Cardiology",
        cost=500,
        people_reviews="Excellent hospital with great staff",
        icu_facilities=True,
        distance_medicals=2.5,
        distance_hotels=1.0,
        years_of_experience=15,
        hospital_size="Large",
        waiting_time=30,
        technology_equipment="Advanced",
        emergency_response_time=10,
        specialized_units=["Cardiac Care", "Emergency Medicine"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.9,
        patient_satisfaction=0.85,
        staff_patient_ratio="1:5",
        avg_length_of_stay=5,
        availability_specialists=True,
        insurance_coverage=True
    ),
    Hospital(
        name="Hospital B",
        doctor_speciality="Orthopedics",
        cost=800,
        people_reviews="Good hospital, but waiting times are long",
        icu_facilities=True,
        distance_medicals=3.2,
        distance_hotels=0.8,
        years_of_experience=10,
        hospital_size="Medium",
        waiting_time=45,
        technology_equipment="Moderate",
        emergency_response_time=15,
        specialized_units=["Orthopedic Surgery", "Physical Therapy"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.85,
        patient_satisfaction=0.75,
        staff_patient_ratio="1:4",
        avg_length_of_stay=6,
        availability_specialists=True,
        insurance_coverage=True
    )
]
