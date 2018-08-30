"""
   Module defines views
"""
from flask import jsonify, request
from flask.views import MethodView
from models.database_model import DatabaseTransaction
import re
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

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
        keys = ("user_name", "email", "password")
        if not set(keys).issubset(set(request.json)):
            return jsonify({'New answer file': 'Your request has Empty feilds'}), 400
        if request.json['user_name'] =="":
            return jsonify({'user name': 'enter user_name'}), 400
        if request.json['email'] =="":
            return jsonify({'email': 'enter email'}), 400
        if request.json['password'] == "":
            return jsonify({'Password': 'Password should not contain any spaces'}), 400
        if (' ' in request.json['password']) == True:
            return jsonify({'Password': 'Password should not contain any spaces'}), 400
        if len(request.json['password'])<8:
            return jsonify({'Password': 'Your password should be more than 8 digits'}), 400        
        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if not re.match(pattern, request.json['email']):
            return jsonify({'email': 'Enter right format of email thanks'}), 400
        new_user = DatabaseTransaction()
        user_details = new_user.insert_new_user(request.json['user_name'], request.json['email'], request.json['password'])
        return jsonify({'Sign up message': user_details}), 201

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
        keys = ("email", "password")
        if not set(keys).issubset(set(request.json)):
            return jsonify({'login Message': 'Your request has Empty feilds'}), 400
        if request.json["email"] == "":
            return jsonify({'Missing email': 'Ennter email'}), 400
        if request.json["password"] == "":
            return jsonify({'Missing password': 'Enter password'}), 400
        login_user = DatabaseTransaction()
        login_data = login_user.fetch_password(request.json['email'], request.json['password'])
        return jsonify({"Login Message": login_data}), 200

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
        return jsonify({"Question": questions_list})

class NewQuestion(MethodView):
    """
       
    """

    def post(self):
        keys = ("user_id", "question")
        if not set(keys).issubset(set(request.json)):
            return jsonify({'Add question Message': 'Your request has Empty feilds'}), 400
        if request.json["user_id"] == "":
            return jsonify({'Missing user_id': 'Enter user_id'}), 400
        if request.json["question"] == "":
            return jsonify({'Missing question': 'Enter question'}), 400
        new_question = DatabaseTransaction() 
        new_question_data = new_question.insert_new_question(request.json['user_id'], request.json['question'])
        return jsonify({'New question': new_question_data}), 201

class NewAnswer(MethodView):
    """
        Add An answer to a question
    """    
    def post(self, question_id):
        keys = ("user_id", "answer")
        if not set(keys).issubset(set(request.json)):
            return jsonify({'Message': 'Your request has Empty feilds'}), 400
        if request.json["user_id"] == "":
            return jsonify({'Missing user_id': 'Enter user_id'}), 400
        if request.json["answer"] == "":
            return jsonify({'Missing answer': 'Enter answer'}), 400
        new_answer = DatabaseTransaction() 
        new_answer_data = new_answer.insert_new_answer(question_id, request.json['user_id'], request.json['answer'])
        return jsonify({'Answer': new_answer_data}), 201