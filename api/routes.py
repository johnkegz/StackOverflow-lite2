"""
   Class for defining url routes
"""
from controllers.main_views import Account


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
        url.add_url_rule('/auth/signup', view_func=Account.as_view('signup'), methods=['POST',])

                                             