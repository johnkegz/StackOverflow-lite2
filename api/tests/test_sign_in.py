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
    def test_login(self):
        """
            Method for tesing the post function which logins in a user
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="ben", password="ben")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"])

    def test_login2(self):
        """
            Method for tesing the post function which logins in a user
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="jgo@gmail.com", password = "18181818")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["message"])

    def test_login3(self):
        """
            Method for tesing the post function which logins in a user
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="", password = "18181818")))
        
        self.assertEqual(result.status_code, 400)
        
        
    def test_login3(self):
        """
            Method for tesing the post function which logins in a user
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="", password = "18181818")))
        
        self.assertEqual(result.status_code, 400)