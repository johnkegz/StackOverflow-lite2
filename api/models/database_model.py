"""
   Module for processing logic for endpoints
"""
import psycopg2
# from .question_answer_class import User


class DatabaseConnection:
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
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        for user in users:
            if user[1]==user_name and user[3] == password:
                return user[1]
        return "login has failed"
    def all_questions(self):
        self.cursor.execute("SELECT * FROM users")
        questions = self.cursor.fetchall()
        question_list = []
        for question in questions:            
            question_list.append(question)
        return question_list
