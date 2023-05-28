import pinecone
import numpy as np
from citz_pref import collect_citizen_preferences
from data import hospital_dataset
from data import Hospital

pinecone.init(api_key="A_P_I_K_E_Y")
index_name = "hospital-recommendation"
pinecone.create_index(name=index_name, dimension=100, metric="cosine")

index = pinecone.Index(index_name=index_name)
embeddings = []

def delete_index():
    pinecone.delete_index(index_name=index_name)
    pinecone.deinit()