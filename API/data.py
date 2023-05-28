class Hospital:
    def __init__(self, id, name, doctor_speciality, phone, cost, icu_facilities, years_of_experience, specialized_units, infection_control_measures, accreditation, surgical_success_rates, patient_satisfaction, insurance_coverage):
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

hospital_dataset = [
    Hospital(
        id = 1, 
        name = "Hospotal 1", 
        doctor_speciality = "Orthopedics", 
        phone = "1213141516"
        cost = 12000, 
        icu_facilities=True, 
        years_of_experience=15, 
        specialized_units=["Orthopedic Surgery", "Physical Therapy"], 
        infection_control_measures=True, 
        accreditation=True, 
        surgical_success_rates=0.92, 
        patient_satisfaction=0.85,
        insurance_coverage=True
        
    )
]
