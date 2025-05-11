"""
Tests for the knowledge_base module.
"""

import unittest
import sys
import os

# Add the parent directory to the path to import the src module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.knowledge_base import infer_disease, get_disease_symptoms, get_all_symptoms

class TestKnowledgeBase(unittest.TestCase):
    """Test cases for the knowledge base module."""
    
    def test_get_all_symptoms(self):
        """Test that get_all_symptoms returns a non-empty list."""
        symptoms = get_all_symptoms()
        self.assertIsInstance(symptoms, list)
        self.assertTrue(len(symptoms) > 0)
    
    def test_get_disease_symptoms(self):
        """Test getting symptoms for specific diseases."""
        flu_symptoms = get_disease_symptoms("flu")
        self.assertEqual(set(flu_symptoms), {"fever", "cough", "sore throat"})
        
        covid_symptoms = get_disease_symptoms("covid19")
        self.assertEqual(set(covid_symptoms), {"fever", "cough", "shortness_of_breath", "loss_of_taste"})
        
        # Test non-existent disease
        nonexistent = get_disease_symptoms("nonexistent_disease")
        self.assertEqual(nonexistent, [])
    
    def test_infer_disease_flu(self):
        """Test flu diagnosis."""
        symptoms = ["fever", "cough", "sore throat", "headache"]
        diseases = infer_disease(symptoms)
        self.assertIn("flu", diseases)
    
    def test_infer_disease_covid(self):
        """Test COVID-19 diagnosis."""
        symptoms = ["fever", "cough", "shortness_of_breath", "loss_of_taste"]
        diseases = infer_disease(symptoms)
        self.assertIn("covid19", diseases)
    
    def test_infer_disease_multiple(self):
        """Test diagnosing multiple diseases from overlapping symptoms."""
        # Symptoms for both flu and strep throat
        symptoms = ["fever", "cough", "sore throat", "swollen lymph nodes"]
        diseases = infer_disease(symptoms)
        self.assertIn("flu", diseases)
        self.assertIn("strep_throat", diseases)
    
    def test_infer_disease_none(self):
        """Test no disease matches insufficient symptoms."""
        symptoms = ["headache", "dizziness"]
        diseases = infer_disease(symptoms)
        self.assertEqual(diseases, [])

if __name__ == '__main__':
    unittest.main()