from app import db


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    athletes = db.relationship('Athlete', backref='country', lazy=True)
    medals = db.relationship('Medal', backref='country', lazy=True)
