"""
   Module defines views
"""
from flask import jsonify, request
from flask.views import MethodView
from models.view_logic import QuestionAnswer


class Login(MethodView):
    """
       Class for logging in the user
    """
    def post(self):
        """
           Method for logging in  user
           params: json requests
           response: json data
        """
        login_user = QuestionAnswer()
        login_data = login_user.fetch_password(request.json['user_name'], request.json['password'])
        return jsonify({"Welcome": login_data})

