"""
   Module defines views
"""
from flask import jsonify, request
from flask.views import MethodView
from models.database_model import DatabaseTransaction
import re
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity


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
        
        if (' ' in request.json['user_name']) == True:
            return jsonify({'message': 'user_name should not contain any spaces'}), 400

        if request.json['email'] =="":
            return jsonify({'email': 'enter email'}), 400
        
        if (' ' in request.json['email']) == True:
            return jsonify({'message': 'email should not contain any spaces'}), 400

        if request.json['password'] == "":
            return jsonify({'message': 'password should not contain any spaces'}), 400

        if (' ' in request.json['password']) == True:
            return jsonify({'Password': 'Password should not contain any spaces'}), 400

        if len(request.json['password'])<8:
            return jsonify({'Password': 'Your password should be more than 8 digits'}), 400

        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if not re.match(pattern, request.json['email']):
            return jsonify({'email': 'Enter right format of email thanks'}), 400

        new_user = DatabaseTransaction()
        user_details = new_user.insert_new_user(request.json['user_name'], request.json['email'], request.json['password'])
        if user_details == "email exits friend":
            return jsonify({'message': user_details}), 401

        return jsonify({'message': user_details}), 201


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
            return jsonify({'message': 'Your request has Empty feilds'}), 400

        if request.json["email"] == "":
            return jsonify({'message': 'Ennter email'}), 400
        
        if (' ' in request.json['email']) == True:
            return jsonify({'message': 'email should not contain any spaces'}), 400

        if request.json["password"] == "":
            return jsonify({'message': 'Enter password'}), 400

        login_user = DatabaseTransaction()
        user_id = login_user.fetch_password(request.json['email'], request.json['password'])

        if user_id:
            return jsonify({
                "access_token" : create_access_token(identity = user_id),
                "message": "Login successful"
            }), 200

        return jsonify({"message": "Wrong username or passwerd"}), 401

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
            if questions_list == "No question available":
                return jsonify({"Question": questions_list}), 404
            return jsonify({"Question": questions_list})

        question_object = DatabaseTransaction()        
        questions_list =  question_object.get_one_question(question_id)
        if questions_list == "Not available":
            return jsonify({"Question": questions_list}), 404
        return jsonify({"Question": questions_list})


class NewQuestion(MethodView):
    """
        Method for inserting a new question
    """
    @jwt_required
    def post(self):
        if not request.json['question']:
            return jsonify({'message': "The 'question' field should not be empty"}), 400

        if request.json["question"] == "":
            return jsonify({'Missing question': 'Enter question'}), 400

        user_id = get_jwt_identity()
        new_question = DatabaseTransaction() 
        new_question_data = new_question.insert_new_question(str(user_id), request.json['question'].strip())

        if new_question_data == "question exits friend":
            return jsonify({'message': "question was not added"}), 401
        return jsonify({'message': new_question_data}), 201
            
        

class NewAnswer(MethodView):
    """
        Add An answer to a question
    """
    @jwt_required
    def post(self, question_id):
        
        if not request.json["answer"]:
            return jsonify({'message': 'Your request has Empty feilds'}), 400
        
        if request.json["answer"] == "":
            return jsonify({'missing answer': 'Enter answer'}), 400

        user_id = get_jwt_identity()
        new_answer = DatabaseTransaction() 
        new_answer_data = new_answer.insert_new_answer(question_id, user_id, request.json['answer'].strip())
        return jsonify({'answer': new_answer_data}), 201


class DeleteQuestion(MethodView):
    """
       Class for deleting a question
    """
    @jwt_required
    def delete(self, question_id):
        """
           Method for deleting a question
        """
        user_id = get_jwt_identity()
        new_answer = DatabaseTransaction()
        new_answer_data = new_answer.delete_question(question_id, str(user_id))
        return jsonify({
            'Delete response': new_answer_data
            })


class AcceptAnswer(MethodView):
    """
       Class for accepting answer
    """

    def put(self, question_id, answer_id):
        if request.json["user_action"] == "update":
            accept = DatabaseTransaction() 
            updated_data = accept.update_answer(question_id, answer_id, request.json["new_answer"])
            return jsonify({
                'message': updated_data
                })

        status = "TRUE"
        accept = DatabaseTransaction() 
        accepted_data = accept.accept_answer(question_id, answer_id, status)
        return jsonify({
            'message': accepted_data
            })