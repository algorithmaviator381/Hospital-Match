def collect_citizen_preferences():
    preferences = {}
    
    print("Welcome to the Citizen Preference Collection")
    print("Please provide your preferences for the following characteristics:")
    
    preferences["doctor_speciality"] = input("Doctor Speciality: ")
    preferences["cost"] = float(input("Cost (in dollars): "))
    preferences["available_beds"] = int(input("Number of Available Beds: "))
    preferences["staff_quality"] = float(input("Staff Quality (on a scale of 1-5): "))
    preferences["icu_facilities"] = input("ICU Facilities (Yes/No): ").lower() == "yes"
    preferences["distance_medicals"] = float(input("Distance from Nearby Medicals (in miles): "))
    preferences["distance_hotels"] = float(input("Distance from Nearby Hotels (in miles): "))
    preferences["years_of_experience"] = int(input("Years of Experience of Doctors: "))
    
    # Add more preferences as needed
    
    return preferences

# Example usage:
citizen_preferences = collect_citizen_preferences()
print(citizen_preferences)
