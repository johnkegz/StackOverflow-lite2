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
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="ben", email="k@gmail.com",
                                                         password="bpeneeee")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 401)
        self.assertTrue(result.json["message"])

    def test_sign2(self):
        """
            Method for tesing the post function which posts a adds a new user
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(
                                                         password="bpeneeee")))
        
        self.assertEqual(result.status_code, 400)
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('New answer file', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["New answer file"])


    def test_sign44(self):
        """
            Method for tesing the post function which posts a adds a new user
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="", email="k@gmail.com",
                                                         password="bpeneeee")))        
        
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('user name', respond)        
        self.assertTrue(result.json["user name"])
            

    def test_sign3(self):
        """
            Method for tesing the post function which posts a adds a new user
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name  = "john", email = "jgo@gmail.com", password = "18181818")))
        
        self.assertEqual(result.status_code, 401)
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 401)
        self.assertTrue(result.json['message'])

    def test_sign5(self):
        """
            Method for tesing the post function which posts a adds a new user
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="kalaas", email="",
                                                         password="bpeneeee")))        
        
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('email', respond)        
        self.assertTrue(result.json["email"])

    def test_sign6(self):
        """
            Method for tesing the post function which posts a adds a new user
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="kalaas", email="j ohn@gmail.com",
                                                         password="d f")))        
        
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)        
        self.assertTrue(result.json["message"])
            