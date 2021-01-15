from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

from views import *

if __name__ == "__main__":
    app.run(host='0.0.0.0')