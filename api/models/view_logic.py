"""
   Module for processing logic for endpoints
"""
import psycopg2
# from .question_answer_class import User


class QuestionAnswer:
    """
       Class for processing logic for endpoints for login
    """
    def __init__ (self):
        try:
            self.connection = psycopg2.connect(dbname='stackoverflow', user='kegz', password='kegz', host='localhost', port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except(Exception, psycopg2.DatabaseError) as e:
            print(e)
            
    def fetch_password(self, user_name, password):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        for user in users:
            if user[1]==user_name and user[3] == password:
                return user[1]
        return "login has failed"
    