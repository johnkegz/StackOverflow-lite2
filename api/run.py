"""
   Module for starting/ running the app
"""
from flask import Flask
from routes import GetRoutes
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
GetRoutes.fetch_routes(app)
if __name__ == '__main__':
    app.run()
    