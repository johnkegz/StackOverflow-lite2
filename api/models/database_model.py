"""
   Module for processing logic for endpoints
"""
import time
import datetime
import psycopg2
import jwt

class DatabaseTransaction:
    """
       Class for processing logic for endpoints for new user..
    """
    def __init__ (self):
        try:
            self.connection = psycopg2.connect(dbname='stackoverflow', user='kegz', password='kegz', host='localhost', port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()                      
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
    def insert_new_user(self, user_name, email, password):
        try:
            insert_item = "INSERT INTO users(user_name, email, password) VALUES('"+user_name+"', '"+email+"', '"+password+"')"
           
            self.cursor.execute(insert_item)
            return "you have successfully created an account"
        except:
            return "you have Failed to created an account"
    def fetch_password(self, user_name, password):
        try:
            
            self.cursor.execute("SELECT * FROM users")
            users = self.cursor.fetchall()
            for user in users:
                if user[1]==user_name and user[3] == password:
                    # token = jwt.encode({'user': user_name, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)})
                    # return token
                    return "successfull login"
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
               print(question)
            
            
            return question_list

        except(Exception, psycopg2.DatabaseError) as e:
            print(e)     
    def get_one_question(self, entered_question_id):        
        
        try:
            self.cursor.execute("SELECT * FROM questions WHERE question_id = %s", [entered_question_id])
            keys = ["question_id", "user_id","questions","question_date"]
            question = self.cursor.fetchone()
            return dict(zip(keys, question))    
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)   
    