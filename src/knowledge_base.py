"""
knowledge_base.py - Disease knowledge base using First Order Logic principles

This module contains the knowledge base for the healthcare diagnostic chatbot.
It defines the symptoms associated with each disease according to FOL rules:

FOL Rules converted to English:
1. A person has the flu if they have fever, cough, and sore throat.
2. A person has the common cold if they have sneezing, runny nose, and mild fever.
3. A person has malaria if they have fever, chills, sweating, and headache.
4. A person has COVID-19 if they have fever, cough, shortness of breath, and loss of taste.
5. A person has strep throat if they have sore throat, swollen lymph nodes, and fever.
"""

# Define the knowledge base using a dictionary where:
# - Each key is a disease
# - Each value is a list of symptoms required for that disease
KNOWLEDGE_BASE = {
    "flu": ["fever", "cough", "sore throat"],
    "common_cold": ["sneezing", "runny nose", "mild fever"],
    "malaria": ["fever", "chills", "sweating", "headache"],
    "covid19": ["fever", "cough", "shortness_of_breath", "loss_of_taste"],
    "strep_throat": ["sore throat", "swollen lymph nodes", "fever"]
}

# List of all possible symptoms from the knowledge base
# This can be used for symptom validation or suggestion
ALL_SYMPTOMS = set()
for symptoms in KNOWLEDGE_BASE.values():
    ALL_SYMPTOMS.update(symptoms)
ALL_SYMPTOMS = sorted(list(ALL_SYMPTOMS))

def get_all_symptoms():
    """Returns a sorted list of all symptoms in the knowledge base."""
    return ALL_SYMPTOMS

def get_disease_symptoms(disease):
    """
    Returns the symptoms associated with a specific disease.
    
    Args:
        disease (str): The name of the disease
        
    Returns:
        list: List of symptoms for the disease or empty list if disease not found
    """
    return KNOWLEDGE_BASE.get(disease, [])

def infer_disease(user_symptoms):
    """
    Uses FOL-style rules to infer possible diseases based on user symptoms.
    
    Args:
        user_symptoms (list): List of symptoms reported by the user
        
    Returns:
        list: List of possible diseases based on reported symptoms
    """
    possible_diseases = []

    # Loop through the knowledge base and apply FOL-style rule:
    # If all symptoms of the disease exist in the user input, add the disease to the list
    for disease, disease_symptoms in KNOWLEDGE_BASE.items():
        if all(symptom in user_symptoms for symptom in disease_symptoms):
            possible_diseases.append(disease)

    return possible_diseases