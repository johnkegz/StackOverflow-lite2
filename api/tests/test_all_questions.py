"""
    Module for making tests on the app for sign in
"""
import unittest
import json
from run import app
class TestViews(unittest.TestCase):
    """"
        Class for making tests on sign in
        params: unittest.testCase
    """

    def setUp(self):
        """
           Method for making the client object
        """
        self.client = app.test_client

    def test_fetch_all_questions(self):
        """
           Method for tesing the get function which returns all questions
        """
        result = self.client().get('/api/v1/questions')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 404)
        self.assertIn('Question', respond)
        self.assertIsInstance(respond, dict)
    