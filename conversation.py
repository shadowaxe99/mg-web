```python
import json
from datetime import datetime
from api.utils import send_message_to_ai, format_message
from db.database import save_conversation, get_conversation

# Constants
INFLUENCER_NAME = "Michael Gruen"
AI_PERSONA = {
    "style": "brash, in-your-face",
    "tone": "confident and audacious",
    "mannerisms": "liberal use of profanity, internet slang, and divisive hot-takes"
}

class Conversation:
    def __init__(self, user_id):
        self.user_id = user_id
        self.messages = []
        self.active = True

    def add_message(self, sender, text):
        timestamp = datetime.now().isoformat()
        message = {
            "sender": sender,
            "text": text,
            "timestamp": timestamp
        }
        self.messages.append(message)
        save_conversation(self.user_id, self.messages)

    def get_messages(self):
        return get_conversation(self.user_id)

    def send_message(self, text):
        self.add_message("fan", text)
        response = send_message_to_ai(text, AI_PERSONA)
        self.add_message("ai_influencer", response)

    def end_conversation(self):
        self.active = False
        # Additional cleanup or archiving actions can be added here

def start_conversation(user_id):
    conversation = Conversation(user_id)
    return conversation

def handle_message(conversation_id, text):
    conversation = Conversation(conversation_id)
    conversation.send_message(text)
    return conversation.get_messages()

def format_conversation_for_display(conversation_id):
    conversation = Conversation(conversation_id)
    messages = conversation.get_messages()
    formatted_messages = [format_message(m) for m in messages]
    return json.dumps(formatted_messages)

# Example usage:
# conversation = start_conversation(user_id=1)
# conversation.send_message("Yooo Michael! Big fan of the empire you're building over here, major inspiration")
# print(format_conversation_for_display(conversation_id=1))
```