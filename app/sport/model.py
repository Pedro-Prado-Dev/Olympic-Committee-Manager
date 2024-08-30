from app import db


class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    team_event = db.Column(db.Boolean, nullable=False, default=False)
    athletes = db.relationship('Athlete', backref='sport', lazy=True)
