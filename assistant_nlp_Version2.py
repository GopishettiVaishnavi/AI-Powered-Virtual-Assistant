import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_response(user_message):
    # Connect to OpenAI GPT or any NLP model
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_message}],
        max_tokens=150
    )
    return completion.choices[0].message["content"].strip()