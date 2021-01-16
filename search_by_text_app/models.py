from app import db

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rubrics = db.Column(db.PickleType)
    text = db.Column(db.Text)
    created_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Text id: {0}, text: {1}>'.format(self.id, self.text)