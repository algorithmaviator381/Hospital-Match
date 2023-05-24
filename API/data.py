class Hospital:
    def __init__(self, name, doctor_speciality, cost, available_beds, staff_quality, people_reviews, icu_facilities, distance_medicals, distance_hotels, years_of_experience, hospital_size, waiting_time, technology_equipment, emergency_response_time, specialized_units, infection_control_measures, accreditation, surgical_success_rates, patient_satisfaction, staff_patient_ratio, avg_length_of_stay, availability_specialists, research_innovation, community_outreach, insurance_coverage):
        self.name = name
        self.doctor_speciality = doctor_speciality
        self.cost = cost
        self.available_beds = available_beds
        self.staff_quality = staff_quality
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
        self.research_innovation = research_innovation
        self.community_outreach = community_outreach
        self.insurance_coverage = insurance_coverage


hospitals = [
    Hospital(
        name="Hospital A",
        doctor_speciality="Cardiology",
        cost=500,
        available_beds=50,
        staff_quality=4.5,
        people_reviews=100,
        icu_facilities=True,
        distance_medicals=1.5,
        distance_hotels=0.8,
        years_of_experience=15,
        hospital_size=10000,
        waiting_time=30,
        technology_equipment=True,
        emergency_response_time=10,
        specialized_units=["Pediatrics", "Orthopedics"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.9,
        patient_satisfaction=4.7,
        staff_patient_ratio=1:5,
        avg_length_of_stay=5,
        availability_specialists=["Cardiologist", "Orthopedic Surgeon"],
        research_innovation=True,
        community_outreach=True,
        insurance_coverage=["Aetna", "Blue Cross"]
    )
]