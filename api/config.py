"""
   Module for for defining the configurations
"""  
class Config(object):
    """
       Method for defining the default environment
    """  
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'kalyango'

class DevelopmentConfig(Config):
    """
       Method for defining the development environment
    """   
    DEBUG = True
    TESTING = False
    ENV = "development"
    SECRET_KEY = 'kalyango'
    
