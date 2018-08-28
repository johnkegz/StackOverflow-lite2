"""
   Class for defining url routes
"""
from controllers.main_views import Login


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
        
        url.add_url_rule('/auth/login', view_func=Login.as_view('Login'), methods=['POST'])

                                             