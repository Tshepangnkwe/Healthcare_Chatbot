"""
Healthcare diagnostic chatbot implementation

This module contains the main chatbot functionality for interacting with users,
getting symptoms, and providing diagnoses and recommendations.
"""

from src.knowledge_base import infer_disease, get_all_symptoms
from src.advice_base import format_advice

def get_user_symptoms():
    """
    Prompts the user for their symptoms and returns a cleaned list.
    
    Returns:
        list: List of cleaned and normalized user symptoms
    """
    print("\n Welcome to HealthBot! ")
    print(" Enter your symptoms (comma-separated): ")
    
    try:
        user_input = input("Symptoms: ").lower()
        
        # Clean and split the input
        symptoms = [symptom.strip() for symptom in user_input.split(",") if symptom.strip()]
        
        if not symptoms:
            print(" No symptoms entered. Please try again.")
            return get_user_symptoms()
            
        return symptoms
    except KeyboardInterrupt:
        print("\n\n Exiting the chatbot. Goodbye!")
        exit(0)
    except Exception as e:
        print(f" Error processing input: {e}")
        print(" Please try again.")
        return get_user_symptoms()

def suggest_similar_symptoms(user_symptoms):
    """
    Suggests possible symptoms if the user's input doesn't match known symptoms.
    
    Args:
        user_symptoms (list): List of symptoms entered by the user
        
    Returns:
        dict: Dictionary mapping user symptoms to suggestions
    """
    all_symptoms = get_all_symptoms()
    suggestions = {}
    
    for symptom in user_symptoms:
        if symptom not in all_symptoms:
            # Find similar symptoms
            similar = [s for s in all_symptoms if symptom in s or s in symptom]
            if similar:
                suggestions[symptom] = similar
    
    return suggestions

def display_diagnosis(diseases):
    """
    Displays the diagnosis and advice for identified diseases.
    
    Args:
        diseases (list): List of diagnosed diseases
    """
    if diseases:
        print("\n Based on your symptoms, you might have:")
        for disease in diseases:
            print(f"- {disease.title()}")
            print(f"  Advice: {format_advice(disease)}")
        print("\n Remember: This is not a professional medical diagnosis.")
        print(" Please consult a healthcare professional for proper evaluation.")
    else:
        print("\n No matching disease found for your symptoms.")
        print(" Please consult a healthcare professional for proper evaluation.")

def run_chatbot():
    """
    Main function to run the chatbot.
    """
    try:
        # Get user symptoms
        user_symptoms = get_user_symptoms()
        print(f"\n You entered: {', '.join(user_symptoms)}")
        
        # Check for similar symptoms and suggest alternatives
        suggestions = suggest_similar_symptoms(user_symptoms)
        if suggestions:
            print("\n Some of your symptoms might be spelled differently in our database:")
            for symptom, similar in suggestions.items():
                print(f" - '{symptom}' - did you mean: {', '.join(similar)}?")
            
            print("\n Please try again with the suggested symptoms if needed.")
        
        # Infer diseases based on symptoms
        diseases = infer_disease(user_symptoms)
        
        # Display diagnosis and advice
        display_diagnosis(diseases)
        
        # Ask if the user wants to check for more symptoms
        print("\n Would you like to check for other symptoms? (yes/no)")
        choice = input(" > ").lower().strip()
        if choice in ['yes', 'y']:
            run_chatbot()
        else:
            print("\n Thank you for using HealthBot. Take care!")
            
    except KeyboardInterrupt:
        print("\n\n Exiting the chatbot. Goodbye!")
    except Exception as e:
        print(f"\n An error occurred: {e}")
        print(" Please try again.")

if __name__ == "__main__":
    run_chatbot()