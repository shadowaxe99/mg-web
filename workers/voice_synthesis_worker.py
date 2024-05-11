```python
import os
import requests
from api.exceptions import VoiceSynthesisException

class VoiceSynthesisWorker:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('ELEVEN_LABS_API_KEY')
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        self.base_url = 'https://api.elevenlabs.io'

    def synthesize_speech(self, text, voice_id='michael-gruen-voice'):
        """
        Synthesize speech using Eleven Labs API with the given text and voice ID.
        """
        payload = {
            'text': text,
            'voiceId': voice_id
        }
        response = requests.post(f'{self.base_url}/synthesize', headers=self.headers, json=payload)

        if response.status_code != 200:
            raise VoiceSynthesisException(f"Failed to synthesize speech: {response.text}")

        return response.content

    def save_speech_to_file(self, speech_data, file_path):
        """
        Save the synthesized speech data to a file.
        """
        with open(file_path, 'wb') as audio_file:
            audio_file.write(speech_data)

# Example usage:
# worker = VoiceSynthesisWorker()
# try:
#     speech_data = worker.synthesize_speech("What's poppin' my guy? Just secured this crazy deal for a new AI startup.")
#     worker.save_speech_to_file(speech_data, 'output.mp3')
# except VoiceSynthesisException as e:
#     print(e)
```