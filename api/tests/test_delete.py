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
        result = self.client().delete('/api/v1/Delete /questions/6')
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('msg', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 401)
        self.assertTrue(result.json["msg"])