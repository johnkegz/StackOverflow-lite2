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
        conn = None
        try:
            self.connection = psycopg2.connect(dbname='stackoverflow', user='kegz', password='kegz', host='localhost', port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            for command in commands:
                print(command)
                self.cursor.execute(command)
            cursor.close()                     
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)        
        
    def insert_new_user(self, user_name, email, password):
        try:
            self.cursor.execute("SELECT * FROM users WHERE email = %s", [email])
            check_email = self.cursor.fetchone()
            if check_email:
                return "email exits friend"
            insert_item = "INSERT INTO users(user_name, email, password) VALUES('"+user_name+"', '"+email+"', '"+password+"')"
            self.cursor.execute(insert_item)
            return "you have successfully created an account"
        except:
            return "you have Failed to created an account"
    def fetch_password(self, email, password):
        try:
            
            self.cursor.execute("SELECT * FROM users")
            users = self.cursor.fetchall()
            for user in users:
                if user[2]==email and user[3] == password:
                    token = jwt.encode({'user': user[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, "kalyango").decode()
                    return token
                    #return "successfull login"
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
            return dict(zip(keys, question))    
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
            insert_answer = "INSERT INTO questions(user_id, questions, question_date) VALUES('"+question_id+"', '"+user_id+"', '"+answer+"', '"+date_time+"')"
            self.cursor.execute(insert_answer)
            return "successfull"                    
        except(Exception, psycopg2.DatabaseError) as e:
            print(e) 
