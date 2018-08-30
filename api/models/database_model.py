"""
   Module for processing logic for endpoints
"""
import time
import datetime
import psycopg2
import jwt
from .authentication import Decod
from werkzeug.security import generate_password_hash, check_password_hash


class DatabaseTransaction:
    """
       Class for processing logic for endpoints for new user..
    """
    def __init__ (self):        
        commands = (
            """
            CREATE TABLE IF NOT EXISTS "users" (
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) NOT NULL,
                    password VARCHAR(200) NOT NULL
                    
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "questions" (                    
                    question_id SERIAL PRIMARY KEY,
                    user_id INT REFERENCES users(user_id),
                    questions VARCHAR(100) NOT NULL,
                    question_date date
                                     
                    
                )
            """,
            """
            CREATE TABLE IF NOT EXISTS "answers" (                    
                    answer_id SERIAL PRIMARY KEY,
                    question_id INT REFERENCES questions(question_id),
                    user_id INT REFERENCES users(user_id),
                    ANSWER VARCHAR(100),                  
                    answer_date date                    
                )
            """,)
        
        try:
            self.connection = psycopg2.connect(dbname='stackoverflow', user='kegz', password='kegz', host='localhost', port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            for command in commands:
                print(command)
                self.cursor.execute(command)
                                
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)        
        
    def insert_new_user(self, user_name, email, password):
        try:
            self.cursor.execute("SELECT * FROM users WHERE email = %s", [email])
            check_email = self.cursor.fetchone()
            hashed_password = generate_password_hash(password, method='sha256')
            if check_email:
                return "email exits friend"
            insert_item = "INSERT INTO users(user_name, email, password) VALUES('"+user_name+"', '"+email+"', '"+hashed_password+"')"
            self.cursor.execute(insert_item)
            return "you have successfully created an account"
        except:
            return "you have Failed to created an account"
    def fetch_password(self, email, password):
        try:
            
            self.cursor.execute("SELECT * FROM users")
            users = self.cursor.fetchall()
            for user in users:
                if user[2]==email and check_password_hash(user[3], password):
                    encode_decode = Decod()
                    return encode_decode.encode_token(user[0])
                    #token = jwt.encode({'user': user[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=31)}, "kalyango").decode()
                    
                    # return encode_decode.decode_token(token)
            return "login has failed"
        except(Exception, psycopg2.ProgrammingError) as e:
            print(e) 
    def all_questions(self):
        try:
            quesrtion_stmt = "SELECT * FROM questions"           
            self.cursor.execute(quesrtion_stmt)
            keys = ["question_id", "user_id","questions","question_date"]            
            questions = self.cursor.fetchall()
            question_list = []
            for question in questions:            
               question_list.append(dict(zip(keys, question)))
            if not question_list: 
                return "No question available"                  
            return question_list

        except(Exception, psycopg2.DatabaseError) as e:
            print(e)     
    def get_one_question(self, entered_question_id):        
        
        try:
            self.cursor.execute("SELECT * FROM questions WHERE question_id = %s", [entered_question_id])
            keys = ["question_id", "user_id","questions","question_date"]
            question = self.cursor.fetchone()
            if not question: 
                return "Not available"
            final_amswer_list = []
            final_amswer_list.append(dict(zip(keys, question)))
            final_amswer_list.append(self.all_answers(entered_question_id))
            return final_amswer_list           
            # return self.all_answers(entered_question_id)    
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)   
    def insert_new_question(self, user_id, new_added_questions):
        try:
            time_value = time.time()
            date_time = datetime.datetime.fromtimestamp(time_value).strftime('%Y-%m-%d %H:%M:%S')
            insert_question = "INSERT INTO questions(user_id, questions, question_date) VALUES('"+user_id+"', '"+new_added_questions+"', '"+date_time+"')"
            self.cursor.execute(insert_question)
            return "successfull"                    
        except(Exception, psycopg2.DatabaseError) as e:
            print(e) 
    def insert_new_answer(self, question_id, user_id, answer):
        try:
            time_value = time.time()            
            date_time = datetime.datetime.fromtimestamp(time_value).strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute("SELECT * FROM questions WHERE question_id = %s", [question_id])
            check_question_id = self.cursor.fetchone()
            if not check_question_id:
                return "question doesnot exits friend"
            insert_answer = "INSERT INTO answers(question_id, user_id, answer, answer_date) VALUES('"+question_id+"', '"+user_id+"', '"+answer+"', '"+date_time+"')"
            self.cursor.execute(insert_answer)            
            return "successfully added answer to question"                    
        except(Exception, psycopg2.ProgrammingError) as e:            
            print(e)
            print(date_time)
    def all_answers(self, question_id):
        self.cursor.execute("SELECT * FROM answers WHERE question_id = %s", [question_id])
        keys = ["answer_id", "question_id","user_id", "answer", "answer_date"]
        check_question_id = self.cursor.fetchall()
        all_answer_list = []
        for answer in check_question_id:
            all_answer_list.append(dict(zip(keys, answer)))
        return {"answer(s)":all_answer_list}

