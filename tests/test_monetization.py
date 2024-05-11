```python
import unittest
from api.utils import monetize_feature, handle_monetization_event
from db.database import Database

class TestMonetization(unittest.TestCase):
    def setUp(self):
        # Initialize the database and create a test user
        self.db = Database('db/database.sqlite3')
        self.test_user_id = self.db.create_user('testuser', 'test@example.com', 'password123')

    def test_monetize_feature(self):
        # Test monetizing a feature
        feature_id = self.db.create_feature('AI Late Night After-Hours', 'Exclusive late night talks with AI Michael Gruen', 'premium')
        transaction_id = monetize_feature(self.test_user_id, feature_id, 'NFT Pass')
        self.assertIsNotNone(transaction_id, "Monetization should return a transaction ID")

    def test_handle_monetization_event(self):
        # Test handling a monetization event
        event_type = 'purchase'
        details = {
            'user_id': self.test_user_id,
            'feature_id': self.db.create_feature('AI Capital Pitch Room', 'Pitch your ideas to AI Michael Gruen', 'elite'),
            'payment_method': 'Crypto',
            'amount': 100
        }
        success = handle_monetization_event(event_type, details)
        self.assertTrue(success, "Monetization event should be handled successfully")

    def tearDown(self):
        # Clean up the database
        self.db.delete_user(self.test_user_id)
        self.db.close()

if __name__ == '__main__':
    unittest.main()
```