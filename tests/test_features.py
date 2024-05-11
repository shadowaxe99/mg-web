```python
import unittest
from features import Feature
from db.database import Database

class TestFeatures(unittest.TestCase):
    def setUp(self):
        # Set up a test database connection
        self.db = Database('test_database.sqlite3')
        self.db.create_tables()  # Assuming this method creates the necessary tables for the test database

    def test_feature_creation(self):
        # Test the creation of a feature
        feature_name = "AI Late Night After-Hours"
        description = "Join a 'late night' live audio experience with Michael's AI persona."
        access_level = "premium"
        
        feature = Feature(name=feature_name, description=description, access_level=access_level)
        feature_id = self.db.add_feature(feature)
        
        self.assertIsNotNone(feature_id, "Feature ID should not be None after creation")
        
        # Retrieve the feature from the database and verify its properties
        retrieved_feature = self.db.get_feature(feature_id)
        self.assertEqual(retrieved_feature.name, feature_name, "Feature name should match the created feature")
        self.assertEqual(retrieved_feature.description, description, "Feature description should match the created feature")
        self.assertEqual(retrieved_feature.access_level, access_level, "Feature access level should match the created feature")

    def test_feature_activation(self):
        # Test the activation of a feature
        user_id = 1  # Assuming a user with ID 1 exists
        feature_id = 2  # Assuming a feature with ID 2 exists
        
        activation_success = self.db.activate_feature(user_id, feature_id)
        self.assertTrue(activation_success, "Feature activation should return True on success")

        # Verify that the feature is marked as active for the user
        active_features = self.db.get_active_features(user_id)
        self.assertIn(feature_id, [f.id for f in active_features], "Activated feature should be in the list of active features for the user")

    def tearDown(self):
        # Clean up the test database
        self.db.drop_tables()  # Assuming this method drops all tables in the test database
        self.db.close_connection()

if __name__ == '__main__':
    unittest.main()
```