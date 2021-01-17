from os import path, getenv

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    DEBUG = True 
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False