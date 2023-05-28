def collect_citizen_preferences():
    preferences = {}
    
    print("Welcome to the Citizen Preference Collection")
    print("Please provide your preferences for the following characteristics:\n\n")
    
    preferences["doctor_speciality"] = input("Doctor Speciality: ")
    preferences["cost"] = float(input("Average cost of hospitalization: "))
    preferences["icu_facilities"] = input("ICU Facilities (Yes/No): ").lower() == "yes"
    preferences["years_of_experience"] = int(input("Years of Experience of Doctors: "))
    
    return preferences
