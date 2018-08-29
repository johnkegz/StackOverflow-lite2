"""
   Module defines views
"""
from flask import jsonify, request
from flask.views import MethodView
from models.database_model import DatabaseTransaction

class SignUp(MethodView):
    """
       Class contains method and signupconfiguratons
    """
    def post(self):
        """
           Method for creating new user
           params: json requests
           response: json data
        """
        new_user = DatabaseTransaction()
        user_details = new_user.insert_new_user(request.json['user_name'], request.json['email'], request.json['password'])
        return jsonify({'Thank You buddy': user_details})

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
        login_user = DatabaseTransaction()
        login_data = login_user.fetch_password(request.json['user_name'], request.json['password'])
        return jsonify({"Welcome": login_data})

class GetQuestion(MethodView):
    """
       Class to get all questions
       params: routes
       respone: json data
    """
    def get(self, question_id):
        """
           get method for get requests
           param: route /api/v1/questions and /api/v1/questions/<int:question_id>
           response: json data get_all_questions() and self.get_one_question(question_id)
        """
        if question_id is None:
            question_object = DatabaseTransaction()        
            questions_list =  question_object.all_questions()
            return jsonify({"Questions": questions_list})
        question_object = DatabaseTransaction()        
        questions_list =  question_object.get_one_question(question_id)
        return jsonify({"Questions": questions_list})

