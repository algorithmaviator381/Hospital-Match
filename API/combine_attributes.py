import numpy as np

def attributes_array(hospital):
    attribute_vector = np.array(
        [
            hospital.id,
            hospital.name,   
            hospital.doctor_speciality,
            hospital.phone,
            hospital.cost,
            hospital.icu_facilities,
            hospital.years_of_experience,
            hospital.specialized_units,
            hospital.infection_control_measures,
            hospital.accreditation,
            hospital.surgical_success_rates,
            hospital.patient_satisfaction,
            hospital.insurance_coverage,
            hospital.beds_availability
        ]
    )
    
    return attribute_vector
