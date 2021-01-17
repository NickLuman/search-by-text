from . import db

class Text(db.Model):
    __tablename__ = "texts"

    id = db.Column(db.Integer, primary_key=True)
    rubrics = db.Column(db.PickleType)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, rubrics, text, created_date):
        self.rubrics = rubrics
        self.text = text
        self.created_date = created_date

    def __repr__(self):
        return '<Text id: {0}, text: {1}>'.format(self.id, self.text)   
