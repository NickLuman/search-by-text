from os import path, getenv

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    DEBUG = bool(getenv("DEBUG", False)) 
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(getenv("SQA_TRACK_MODIFICATIONS", False)) 