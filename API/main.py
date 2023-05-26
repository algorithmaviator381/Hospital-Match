from data import Hospital
from citz_pref import collect_citizen_preferences
from vector_database import index, recommend_hospitals, user_preferences

recommended_hospitals = recommend_hospitals(user_preferences, index)

print(recommended_hospitals)