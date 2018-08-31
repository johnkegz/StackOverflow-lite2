"""
   Class for defining url routes
"""
from controllers.views import Login, GetQuestion, SignUp, NewQuestion, NewAnswer, DeleteQuestion, AcceptAnswer


class GetRoutes():
    """
       GetRoutes defines routes
       params:urls
    """
    @staticmethod
    def fetch_routes(url):
        """
           Add url rule defines the routes for http requests
        """
        url.add_url_rule('/auth/signup', view_func=SignUp.as_view('Signup'), methods=['POST',])
        url.add_url_rule('/auth/login', view_func=Login.as_view('Login'), methods=['POST',])
        url.add_url_rule('/questions', view_func=GetQuestion.as_view('questions'), defaults={'question_id': None}, methods=['GET',])
        url.add_url_rule('/questions/<int:question_id>', view_func=GetQuestion.as_view('one_questions'), methods=['Get',])
        url.add_url_rule('/questions', view_func=NewQuestion.as_view('New question'), methods=['POST',])
        url.add_url_rule('/questions/<question_id>/answers', view_func=NewAnswer.as_view('New answer'), methods=['POST',])
        url.add_url_rule('/Delete /questions/<int:question_id>', view_func=DeleteQuestion.as_view('Delete Question'), methods=['DELETE',])
        url.add_url_rule('/questions/<question_id>/answers/<answer_id>', view_func=AcceptAnswer.as_view('Accept answer'), methods=['PUT'])