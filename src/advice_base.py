"""
advice_base.py - Medical advice for diagnosed diseases

This module contains medical recommendations for each disease 
that can be diagnosed by the healthcare chatbot.
"""

# Define the advice base with recommendations for each disease
ADVICE_BASE = {
    "flu": [
        "Get plenty of rest and sleep.",
        "Drink plenty of fluids to prevent dehydration.",
        "Take over-the-counter pain relievers to reduce fever and relieve aches."
    ],
    "common_cold": [
        "Stay hydrated and rest.",
        "Use a humidifier or take a hot shower to relieve congestion.",
        "Try over-the-counter cold medications to alleviate symptoms."
    ],
    "malaria": [
        "Seek immediate medical attention.",
        "Complete the full course of prescribed antimalarial medication.",
        "Use mosquito nets and insect repellent to prevent reinfection."
    ],
    "covid19": [
        "Self-isolate to prevent spreading the virus.",
        "Monitor your oxygen levels with a pulse oximeter.",
        "Contact healthcare professionals if symptoms worsen."
    ],
    "strep_throat": [
        "Complete the full course of prescribed antibiotics.",
        "Use throat lozenges or warm salt water gargles for pain relief.",
        "Rest your voice and stay hydrated."
    ]
}

def get_advice(disease):
    """
    Returns medical advice for a specific disease.
    
    Args:
        disease (str): The name of the disease
        
    Returns:
        list: List of advice recommendations for the disease,
              or default message if disease not found
    """
    return ADVICE_BASE.get(disease, ["Please consult a healthcare professional."])

def format_advice(disease):
    """
    Returns formatted advice string for a specific disease.
    
    Args:
        disease (str): The name of the disease
        
    Returns:
        str: Formatted advice string
    """
    advice_list = get_advice(disease)
    advice_text = "\n    - " + "\n    - ".join(advice_list)
    return advice_text