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
    def test_one_question(self):
        """
            Method for tesing the get function which returns one question
        """
        result = self.client().get('/questions/5')
        result2 = self.client().get('/questions/a')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result2.status_code, 404)
        self.assertIsInstance(respond, dict)