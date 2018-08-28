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
            Method for tesing the post function which posts a adds a new user
        """
        result = self.client().post('/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="ben", email="k@gmail.com",
                                                         password="ben")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Thank You buddy', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["Thank You buddy"])
    