import os

class BaseConfig(object):
    # google maps key 
    API_KEY = "AIzaSyBmJyATYWlxlD3RqLt9UY7J21eHxOvUEws"     
    SECRET_KEY = "whiterabbit"
    CACHE_TYPE = "simple"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True

    # DB settings
    DB_USER = "andreaslykke:postgress"
    DB_PASSWORD = "postgres"
    DB_HOST = "localhost"
    DB_NAME = "sfdb"
    SQLALCHEMY_DATABASE_URI = "postgresql://" + DB_USER + \
                              ":" + DB_PASSWORD + \
                              "@" + DB_HOST + \
                              "/" + DB_NAME

class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True  

    # DB settings
    DB_USER = ""
    DB_PASSWORD = ""
    DB_HOST = ""
    DB_NAME = ""

    if os.environ.get('DATABASE_URL') is None:
        SQLALCHEMY_DATABASE_URI = "postgresql://" + DB_USER + \
                                  ":" + DB_PASSWORD + \
                                  "@" + DB_HOST + \
                                  "/" + DB_NAME
    else:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    CSRF_ENABLED = False

    # DB settings
    DB_USER = "andreaslykke:postgress"
    DB_PASSWORD = "postgres"
    DB_HOST = "localhost"
    DB_NAME = "sfdb"
    SQLALCHEMY_DATABASE_URI = "postgresql://" + DB_USER + \
                              ":" + DB_PASSWORD + \
                              "@" + DB_HOST + \
                              "/" + DB_NAME