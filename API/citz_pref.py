def collect_citizen_preferences():
    preferences = {}
    
    print("Welcome to the Citizen Preference Collection")
    print("Please provide your preferences for the following characteristics:\n\n")
    
    preferences["doctor_speciality"] = input("Doctor Speciality: ")
    preferences["cost"] = float(input("Average cost of hospitalization: "))
    preferences["available_beds"] = int(input("Number of Available Beds: "))
    preferences["icu_facilities"] = input("ICU Facilities (Yes/No): ").lower() == "yes"
    preferences["distance_home"] = float(input("Distance from your home (in km): "))
    preferences["years_of_experience"] = int(input("Years of Experience of Doctors: "))
    
    return preferences

# sample_preference = {
#     "doctor_speciality": "Cardiology",
#     "cost": 600.0,
#     "icu_facilities": True,
#     "distance_home": 5.2,
#     "years_of_experience": 12
# }

citizen_preferences = collect_citizen_preferences()

#citizen_preferences.update(sample_preference)
