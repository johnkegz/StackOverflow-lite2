"""
   Module for processing logic for endpoints
"""
import os
import time
import datetime
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash


class DatabaseTransaction:
    """
       Class for processing logic for endpoints for new user..
    """
    def __init__(self):
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
                    answer VARCHAR(100),
                    answer_date DATE,
                    accepted VARCHAR(10) DEFAULT 'FALSE'
                )
            """,)

        try:
            if(os.getenv("FLASK_ENV")) == "Production":
                self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
            else:
                self.connection = psycopg2.connect(dbname='stackoverflow',
                                                   user='postgres',
                                                   password='',
                                                   host='localhost',
                                                   port='5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            for command in commands:
                self.cursor.execute(command)
        except(Exception, psycopg2.DatabaseError) as error:
            raise error

    def insert_new_user(self, user_name, email, password):
        """
           Method for
        """
        self.cursor.execute("SELECT * FROM users WHERE email = %s", [email])
        check_email = self.cursor.fetchone()
        hashed_password = generate_password_hash(password, method='sha256')
        if check_email:
            return "email exits friend"

        insert_item = "INSERT INTO users(user_name, email, password) VALUES('"+user_name+"', '"+email+"', '"+hashed_password+"')"
        self.cursor.execute(insert_item)
        return "you have successfully created an account"

    def fetch_password(self, email, password):
        """
           Method for
        """
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        for user in users:
            if user[2] == email and check_password_hash(user[3], password):
                return user[0]
        return None

    def all_questions(self):
        """
           Method for
        """
        quesrtion_stmt = "SELECT * FROM questions"
        self.cursor.execute(quesrtion_stmt)
        keys = ["question_id", "user_id", "questions", "question_date"]
        questions = self.cursor.fetchall()
        question_list = []
        for question in questions:
            question_list.append(dict(zip(keys, question)))
        if not question_list:
            return "No question available"

        return question_list

    def get_one_question(self, entered_question_id):
        """
           Method for
        """
        self.cursor.execute("SELECT * FROM questions WHERE question_id = %s", [entered_question_id])
        keys = ["question_id", "user_id", "questions", "question_date"]
        question = self.cursor.fetchone()
        if not question:
            return "Not available"
        final_amswer_list = []
        final_amswer_list.append(dict(zip(keys, question)))
        final_amswer_list.append(self.all_answers(entered_question_id))
        return final_amswer_list

    def insert_new_question(self, user_id, new_added_questions):
        """
           Method for
        """
        time_value = time.time()
        date_time = datetime.datetime.fromtimestamp(time_value).strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute("SELECT * FROM questions WHERE questions = %s", [new_added_questions])
        check_question = self.cursor.fetchone()
        if check_question:
            return "question exits friend"

        insert_question = "INSERT INTO questions(user_id, questions, question_date) VALUES('"+user_id+"', '"+new_added_questions+"', '"+date_time+"')"
        self.cursor.execute(insert_question)
        return "question succcssfully created"

    def insert_new_answer(self, question_id, user_id, answer):
        """
           Method for
        """
        try:
            time_value = time.time()
            date_time = datetime.datetime.fromtimestamp(time_value).strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute("SELECT * FROM questions WHERE question_id = %s", [question_id])
            check_question_id = self.cursor.fetchone()
            if not check_question_id:
                return "question doesnot exits friend"

            insert_answer = "INSERT INTO answers(question_id, user_id, answer, answer_date) VALUES(%s, %s, %s, %s)"
            self.cursor.execute(insert_answer, [question_id, user_id, answer, date_time])
            return "successfully added answer to question"

        except(Exception, psycopg2.ProgrammingError) as error:
            raise error

    def delete_question(self, question_id, question_ower):
        """
           Method for deleting a question
        """
        self.cursor.execute("SELECT * FROM questions WHERE question_id = %s", [question_id])
        check_question_id = self.cursor.fetchone()
        if not check_question_id:
            return "Question doesnot exist"

        self.cursor.execute(
            "DELETE FROM questions WHERE user_id = '"+question_ower+"' and question_id = %s", [question_id])

        self.cursor.execute("SELECT * FROM questions WHERE question_id = %s", [question_id])
        check_question_id = self.cursor.fetchone()
        if not check_question_id:
            return "Question deleted"

        return "Question not deleted because you did not post it thanks"

    def all_answers(self, question_id):
        """
           Method for
        """
        self.cursor.execute("SELECT * FROM answers WHERE question_id = %s", [question_id])
        keys = ["answer_id", "question_id", "user_id", "answer", "answer_date"]
        check_question_id = self.cursor.fetchall()
        all_answer_list = []
        for answer in check_question_id:
            all_answer_list.append(dict(zip(keys, answer)))
        return {
            "answer(s)":all_answer_list
            }

    def update_answer(self, question_id, answer_id, new_answer, user_id):
        """
           Method for updating answer
        """
        print(question_id)
        self.cursor.execute("SELECT * FROM questions WHERE question_id = %s", [question_id])
        check_question_id = self.cursor.fetchone()
        if not check_question_id:
            return "Question doesnot exist"

        self.cursor.execute("SELECT * FROM answers WHERE answer_id = '"+answer_id+"' and question_id = %s", [question_id])
        check_answer_id = self.cursor.fetchone()
        if not check_answer_id:
            return "Question doesnot exist"

        self.cursor.execute("SELECT * FROM answers WHERE user_id = %s", [user_id])
        check_user_id = self.cursor.fetchone()
        if not check_user_id:
            return "you did not post this answer"

        print(new_answer)
        self.cursor.execute("UPDATE answers SET answer = '"+new_answer+"' WHERE  answer_id = '"+answer_id+"' and question_id = %s", [question_id])
        return "answer updated"

    def accept_answer(self, question_id, answer_id, accepted, user_id):
        """
           Method for
        """
        self.cursor.execute("SELECT * FROM questions WHERE question_id = %s", [question_id])
        check_question_id = self.cursor.fetchone()
        if not check_question_id:
            return "Question doesnot exist"

        self.cursor.execute("SELECT * FROM questions WHERE user_id = %s", [user_id])
        check_question_id = self.cursor.fetchone()
        if not check_question_id:
            return "you did not post this question"

        self.cursor.execute("SELECT * FROM answers WHERE answer_id = '"+answer_id+"' and question_id = %s", [question_id])
        check_answer_id = self.cursor.fetchone()
        if not check_answer_id:
            return "Question doesnot exist"

        self.cursor.execute("UPDATE answers SET accepted = '"+accepted+"' WHERE answer_id = '"+answer_id+"' and question_id = %s", [question_id])
        return "answer accepted"
