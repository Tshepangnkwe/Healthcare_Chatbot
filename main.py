"""
Healthcare Diagnostic Chatbot - Main Entry Point
CMPG 313 - Artificial Intelligence

This is the main entry point for the healthcare chatbot application.
It imports the necessary modules and runs the chatbot.
"""

from src.chatbot import run_chatbot

if __name__ == "__main__":
    # Display welcome banner
    print("="*60)
    print("  HEALTHCARE DIAGNOSTIC CHATBOT USING FIRST ORDER LOGIC (FOL)")
    print("  CMPG 313 - Artificial Intelligence")
    print("="*60)
    
    # Run the chatbot
    run_chatbot()