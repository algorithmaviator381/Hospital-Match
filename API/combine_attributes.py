import numpy as np

def combine_attributes(hospital):
    attribute_vector = np.array([
        hospital.cost,
        hospital.icu_facilities,
        hospital.years_of_experience,
        hospital.hospital_size,
        hospital.waiting_time,
        hospital.technology_equipment,
        hospital.emergency_response_time,
        hospital.specialized_units,
        hospital.infection_control_measures,
        hospital.accreditation,
        hospital.surgical_success_rates,
        hospital.patient_satisfaction,
        hospital.staff_patient_ratio,
        hospital.avg_length_of_stay,
        hospital.availability_specialists,
        hospital.insurance_coverage
    ])
    
    return attribute_vector
