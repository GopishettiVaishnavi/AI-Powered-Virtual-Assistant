from .nlp import get_ai_response

def get_virtual_assistant_response(user_message):
    # Here you can add context, user profile, or logic for different intents
    response = get_ai_response(user_message)
    return response