# Healthcare Diagnostic Chatbot

## CMPG 313 - Artificial Intelligence
### First Order Logic (FOL) Based Healthcare Chatbot

This project implements a simple healthcare diagnostic chatbot using First Order Logic (FOL) principles to diagnose common diseases based on reported symptoms.

## Project Structure

```
healthcare_chatbot/
│
├── main.py                # Entry point for the application
├── README.md              # Project documentation
│
├── src/                   # Source code directory
│   ├── __init__.py        # Makes src a Python package
│   ├── knowledge_base.py  # Contains disease rules and symptom mappings
│   ├── advice_base.py     # Contains recommendations for each disease
│   └── chatbot.py         # Contains the chatbot logic and user interaction
│
├── tests/                 # Unit tests
│   ├── __init__.py
│   ├── test_knowledge.py  # Tests for knowledge base
│   └── test_chatbot.py    # Tests for chatbot functionality
│
└── docs/                  # Documentation
    ├── report.pdf         # Assignment report
    └── screenshots/       # Screenshots for different test cases
```

## FOL Rules

The following First Order Logic rules have been implemented:

1. A person has the flu if they have fever, cough, and sore throat.
2. A person has the common cold if they have sneezing, runny nose, and mild fever.
3. A person has malaria if they have fever, chills, sweating, and headache.
4. A person has COVID-19 if they have fever, cough, shortness of breath, and loss of taste.
5. A person has strep throat if they have sore throat, swollen lymph nodes, and fever.

## How to Run

1. Make sure you have Python 3.6 or higher installed
2. Navigate to the project root directory
3. Run the chatbot:

```bash
python main.py
```

## Usage

1. When prompted, enter your symptoms separated by commas
2. The chatbot will analyze your symptoms using FOL rules
3. If a diagnosis is found, the chatbot will display the possible disease(s) and advice
4. You can choose to check for more symptoms or exit

## Enhancement Features

The current implementation includes several features:

1. **Symptom Suggestion**: The chatbot suggests similar symptoms if your entry doesn't match known symptoms
2. **Multiple Disease Detection**: Can diagnose multiple diseases if symptoms match
3. **User-Friendly Interface**: Clear prompts and formatted output for better readability
4. **Error Handling**: Robust error handling for invalid inputs

## Future Enhancements

Potential future enhancements for this project:

1. **Symptom Severity Tracking**: Allow users to rate symptom severity
2. **Medical History Integration**: Consider past medical conditions in diagnosis
3. **Natural Language Processing**: Improve user input processing
4. **Follow-up Questions**: Ask targeted follow-up questions to narrow down diagnoses

## Disclaimer

This chatbot is for educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
