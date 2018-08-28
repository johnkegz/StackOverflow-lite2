"""
   Module for processing logic for endpoints
"""
import psycopg2
# from .question_answer_class import User


class QuestionAnswer:
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
    