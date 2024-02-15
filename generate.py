# Importing Libraries
import google.generativeai as genai

# Selecting the Gemini model and configuring the API key
model = genai.GenerativeModel('gemini-pro')
genai.configure(api_key='your-api-key')

def  generate_content(topic,difficulty,level):
    # Prompting the model to generate content
    data = f"""
     Prompt - Generate 10 multiple choice maths questions on trigonometry and also provide answer.Give Answer in json format                            
    {
    "questions": [
    {
    "question": "What is the value of sin(30°)?",
    "options": ["0.5", "1", "0.75", "0.25"],
    "answer": "0.5"
    },
    {
    "question": "What is the value of cos(45°)?",
    "options": ["0.5", "1", "0.75", "0.25"],
    "answer": "0.75"
    },
    {
    "question": "What is the value of tan(60°)?",
    "options": ["1", "√3", "2", "√2"],
    "answer": "√3"
    },
    {
    "question": "What is the value of sin(90°)?",
    "options": ["0", "1", "0.5", "-1"],
    "answer": "1"
    },
    {
    "question": "What is the value of cos(0°)?",
    "options": ["0", "1", "0.5", "2"],
    "answer": "1"
    },
    {
    "question": "What is the value of tan(0°)?",
    "options": ["0", "1", "undefined", "2"],
    "answer": "0"
    },
    {
    "question": "What is the value of sin(180°)?",
    "options": ["0", "1", "-1", "0.5"],
    "answer": "0"
    },
    {
    "question": "What is the value of cos(270°)?",
    "options": ["0", "1", "-1", "0.5"],
    "answer": "-1"
    },
    {
    "question": "What is the value of tan(360°)?",
    "options": ["0", "1", "undefined", "2"],
    "answer": "0"
    },
    {
    "question": "What is the value of sin(2π)?",
    "options": ["0", "1", "-1", "0.5"],
    "answer": "0"
    }
    ],
    "answers": ["0.5", "0.75", "√3", "1", "1", "0", "0", "-1", "0", "0"]
    }

    Prompt - Generate 10 multiple choice questions on {topic} of {difficulty} of {level} and also provide answer .Give Answer in json format                        
    """

    response = model.generate_content(data)

    return response.text
