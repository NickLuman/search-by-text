from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from elasticsearch import Elasticsearch

app = Flask(__name__)

app.config.from_object("project.config.Config")
app.elasticsearch = Elasticsearch("http://es:9200/")

db = SQLAlchemy(app)