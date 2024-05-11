```python
import openai
from api.exceptions import ChatbotException
from config.config import OPENAI_API_KEY

class ChatbotWorker:
    def __init__(self):
        self.openai_api_key = OPENAI_API_KEY
        self.model = "text-davinci-003"  # or any other suitable model
        self.session_prompt = self._create_initial_prompt()

    def _create_initial_prompt(self):
        return (
            "The following is a conversation with an AI version of Michael Gruen. "
            "Michael is known for his brash, in-your-face style that oozes wealth, exclusivity, "
            "and a rebellious anti-establishment ethos. He is confident and audacious, "
            "often using profanity, internet slang, and divisive hot-takes designed to provoke a reaction. "
            "He flaunts expensive possessions and luxurious experiences, promotes a hardcore entrepreneurial mindset, "
            "and embodies the spirit of Gen Z ambition.\n\n"
        )

    def generate_response(self, message):
        try:
            response = openai.Completion.create(
                engine=self.model,
                prompt=f"{self.session_prompt}{message}\n\n###\n\n",
                max_tokens=150,
                api_key=self.openai_api_key,
                stop=["\n", "###"],
                temperature=0.9
            )
            return response.choices[0].text.strip()
        except Exception as e:
            raise ChatbotException(f"Failed to generate response: {str(e)}")

    def update_session_prompt(self, message, response):
        self.session_prompt += f"Fan: {message}\nAI Influencer (Michael Gruen): {response}\n"

# Example usage:
# chatbot = ChatbotWorker()
# fan_message = "Hey Michael, what's your advice for someone starting their own business?"
# ai_response = chatbot.generate_response(fan_message)
# chatbot.update_session_prompt(fan_message, ai_response)
```