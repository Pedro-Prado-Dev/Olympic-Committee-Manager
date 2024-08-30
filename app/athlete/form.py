from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app.country.model import Country
from app.sport.model import Sport

class AthleteForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    country_id = SelectField('Country', coerce=int, validators=[DataRequired()])
    sport_id = SelectField('Sport', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Save')

    def __init__(self, *args, **kwargs):
        super(AthleteForm, self).__init__(*args, **kwargs)
        self.country_id.choices = [(c.id, c.name) for c in Country.query.all()]
        self.sport_id.choices = [(s.id, s.name) for s in Sport.query.all()]
