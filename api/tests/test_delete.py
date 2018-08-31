"""
    Module for making tests on the app for sign up
"""
import unittest
import json
from run import app
class TestViews(unittest.TestCase):
    """"
        Class for making tests on sign up
        params: unittest.testCase
    """

    def setUp(self):
        """
           Method for making the client object
        """
        self.client = app.test_client
    def test_sign(self):
        """
            Method for tesing the delete function that deletes a question
        """
        result = self.client().delete('/Delete /questions/15')
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Delete response', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["Delete response"])