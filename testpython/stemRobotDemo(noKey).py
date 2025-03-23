import requests
import json

# DeepSeek API key - STEM
API_KEY = 'sk---a5'
API_URL = 'https://api.deepseek.com/v1/chat/completions' 

# Define the headers for the API request
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Define the prompt generation request
def generate_prompt(task_description):
    data = {
        'model': 'deepseek-chat',  # Replace with the correct model name
        'messages': [{'role': 'user', 'content': f"Generate a step-by-step prompt for STEM students to complete the following task on a UBTech Robot: {task_description}"}],
        'max_tokens': 200,
        'temperature': 0.7
    }

    try:
        # Make the API request
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Get task description from the user
task_description = input("Enter the task description for the UBTech Robot: ")

# Generate the prompt
prompt = generate_prompt(task_description)
print("\nGenerated Prompt:\n", prompt)