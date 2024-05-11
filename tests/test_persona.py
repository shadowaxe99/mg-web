```python
import unittest
from persona import Persona

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.influencer_name = "Michael Gruen"
        self.influencer_description = (
            "Michael Gruen is a young, dynamic entrepreneur and influencer who embodies the ambitious spirit of Gen Z. "
            "With an irreverent, edgy persona, Michael engages his audience through a lens of disruption and rejecting traditional norms. "
            "He promotes a hustle-hard mindset while embracing boundary-pushing ideas and aesthetics. "
            "Michael's content showcases his entrepreneurial ventures, luxurious lifestyle, and cutting-edge interests like crypto, AI, and experiential tech."
        )
        self.influencer_content = (
            "Michael's social media (@michaelgruen on Instagram/Twitter/TikTok) features candid, documentary-style vlogs taking viewers behind-the-scenes "
            "of his entrepreneurial projects and luxury experiences like exclusive events, exotic travel adventures, and flexing his impressive product collections "
            "(hypercars, sneakers, watches etc.). His aesthetic combines streetwear fashion with aspirational flexes of wealth and success. "
            "His captions and commentary embrace controversial hot-takes and flaunt his IDGAF attitude."
        )
        self.persona_attributes = {
            "style": "brash, in-your-face",
            "tone": "confident and audacious",
            "mannerisms": "liberal use of profanity, internet slang, and divisive hot-takes",
            "engagement": "flaunting expensive possessions and luxurious experiences",
            "mindset": "hardcore entrepreneurial",
            "vibe": "disruptive and boundary-pushing",
            "voice_for": "Gen Z ambition",
            "stance": "rejecting traditional norms"
        }
        self.persona = Persona(self.influencer_name, self.persona_attributes)

    def test_persona_creation(self):
        self.assertEqual(self.persona.name, self.influencer_name)
        self.assertEqual(self.persona.attributes, self.persona_attributes)

    def test_persona_representation(self):
        expected_representation = (
            f"Persona(name={self.influencer_name}, attributes={self.persona_attributes})"
        )
        self.assertEqual(repr(self.persona), expected_representation)

    def test_persona_engagement(self):
        fan_message = "Yooo Michael! Big fan of the empire you're building over here, major inspiration"
        response = self.persona.respond_to_fan(fan_message)
        self.assertIn("What's poppin' my guy?", response)

if __name__ == '__main__':
    unittest.main()
```