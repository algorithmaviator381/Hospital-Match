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

hospital_dataset = [
    Hospital(
        id=1,
        name="Hospital 1",
        doctor_speciality="Orthopedics",
        phone="1213141516",
        cost=12000,
        icu_facilities=True,
        years_of_experience=15,
        specialized_units=["Orthopedic Surgery", "Physical Therapy"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.92,
        patient_satisfaction=0.85,
        insurance_coverage=True,
        beds_availability=True
    ),
    Hospital(
        id=2,
        name="Hospital 2",
        doctor_speciality="Cardiology",
        phone="1718192021",
        cost=15000,
        icu_facilities=True,
        years_of_experience=20,
        specialized_units=["Cardiac Surgery", "Interventional Cardiology"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.95,
        patient_satisfaction=0.88,
        insurance_coverage=True,
        beds_availability=True
    ),
    Hospital(
        id=3,
        name="Hospital 3",
        doctor_speciality="Gastroenterology",
        phone="2223242526",
        cost=10000,
        icu_facilities=True,
        years_of_experience=12,
        specialized_units=["Endoscopy", "Colorectal Surgery"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.88,
        patient_satisfaction=0.82,
        insurance_coverage=True,
        beds_availability=True
    ),
    Hospital(
        id=4,
        name="Hospital 4",
        doctor_speciality="Oncology",
        phone="2728293031",
        cost=18000,
        icu_facilities=True,
        years_of_experience=18,
        specialized_units=["Medical Oncology", "Radiation Oncology"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.94,
        patient_satisfaction=0.87,
        insurance_coverage=True,
        beds_availability=True
    ),
    Hospital(
        id=5,
        name="Hospital 5",
        doctor_speciality="Neurology",
        phone="3233343536",
        cost=14000,
        icu_facilities=True,
        years_of_experience=16,
        specialized_units=["Neurosurgery", "Stroke Unit"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.90,
        patient_satisfaction=0.84,
        insurance_coverage=True,
        beds_availability=True
    ),
    Hospital(
        id=6,
        name="Hospital 6",
        doctor_speciality="Pediatrics",
        phone="3738394041",
        cost=9000,
        icu_facilities=True,
        years_of_experience=10,
        specialized_units=["Pediatric Intensive Care", "Neonatology"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.89,
        patient_satisfaction=0.86,
        insurance_coverage=True,
        beds_availability=True
    ),
    Hospital(
        id=7,
        name="Hospital 7",
        doctor_speciality="Dermatology",
        phone="4243444546",
        cost=11000,
        icu_facilities=False,
        years_of_experience=8,
        specialized_units=["Cosmetic Dermatology", "Mohs Surgery"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.91,
        patient_satisfaction=0.83,
        insurance_coverage=True,
        beds_availability=True
    ),
    Hospital(
        id=8,
        name="Hospital 8",
        doctor_speciality="Obstetrics and Gynecology",
        phone="4748495051",
        cost=13000,
        icu_facilities=True,
        years_of_experience=14,
        specialized_units=["Maternal-Fetal Medicine", "Reproductive Endocrinology"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.93,
        patient_satisfaction=0.89,
        insurance_coverage=True,
        beds_availability=True
    ),
    Hospital(
        id=9,
        name="Hospital 9",
        doctor_speciality="Ophthalmology",
        phone="5253545556",
        cost=16000,
        icu_facilities=True,
        years_of_experience=17,
        specialized_units=["Cataract Surgery", "Retina Services"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.92,
        patient_satisfaction=0.87,
        insurance_coverage=True,
        beds_availability=True
    ),
    Hospital(
        id=10,
        name="Hospital 10",
        doctor_speciality="ENT (Ear, Nose, and Throat)",
        phone="5758596061",
        cost=10000,
        icu_facilities=True,
        years_of_experience=11,
        specialized_units=["Head and Neck Surgery", "Audiology"],
        infection_control_measures=True,
        accreditation=True,
        surgical_success_rates=0.90,
        patient_satisfaction=0.85,
        insurance_coverage=True,
        beds_availability=True
    )
]
