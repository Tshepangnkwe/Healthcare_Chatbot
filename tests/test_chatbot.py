"""
Tests for the chatbot module.
"""

import unittest
import sys
import os
import io
from unittest.mock import patch

# Add the parent directory to the path to import the src module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chatbot import suggest_similar_symptoms, display_diagnosis

class TestChatbot(unittest.TestCase):
    """Test cases for the chatbot module."""
    
    def test_suggest_similar_symptoms(self):
        """Test symptom suggestion functionality."""
        # Test with a slight misspelling
        user_symptoms = ["fevre", "cough", "headake"]
        suggestions = suggest_similar_symptoms(user_symptoms)
        
        # Should suggest "fever" for "fevre" and "headache" for "headake"
        self.assertTrue("fevre" in suggestions)
        self.assertTrue("headake" in suggestions)
        
        # Test with a correct symptom
        user_symptoms = ["fever", "cough"]
        suggestions = suggest_similar_symptoms(user_symptoms)
        self.assertEqual(suggestions, {})  # No suggestions needed
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_diagnosis_with_diseases(self, mock_stdout):
        """Test displaying diagnosis with identified diseases."""
        diseases = ["flu", "common_cold"]
        display_diagnosis(diseases)
        output = mock_stdout.getvalue()
        
        # Check that both diseases are in the output
        self.assertIn("Flu", output)
        self.assertIn("Common Cold", output)
        self.assertIn("Remember: This is not a professional medical diagnosis", output)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_diagnosis_no_diseases(self, mock_stdout):
        """Test displaying diagnosis with no diseases found."""
        diseases = []
        display_diagnosis(diseases)
        output = mock_stdout.getvalue()
        
        # Check that the no match message is displayed
        self.assertIn("No matching disease found", output)
        self.assertIn("Please consult a healthcare professional", output)

if __name__ == '__main__':
    unittest.main()