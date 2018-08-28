"""
   Module defines views
"""
from flask import jsonify, request
from flask.views import MethodView
from models.view_logic import QuestionAnswer


class Account(MethodView):
    """
       Class contains methods for sign up
    """
    def post(self):
        """
           Method for creating new user
           params: json requests
           response: json data
        """
        new_user = QuestionAnswer()
        user_details = new_user.insert_new_user(request.json['user_name'], request.json['email'], request.json['password'])
        return jsonify({'Thank You buddy': user_details})

