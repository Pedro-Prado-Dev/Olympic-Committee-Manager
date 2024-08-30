from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length
from app.athlete.model import Athlete
from app.sport.model import Sport
from app.country.model import Country


class MedalForm(FlaskForm):
    type = SelectField('Medal Type', choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')],
                       validators=[DataRequired()])
    event = StringField('Event', validators=[DataRequired(), Length(max=100)])
    sport_id = SelectField('Sport', coerce=int, validators=[DataRequired()])
    country_id = SelectField('Country', coerce=int, validators=[DataRequired()])
    athletes = SelectMultipleField('Athletes', coerce=int, validators=[DataRequired()])  # Select multiple athletes
    submit = SubmitField('Save')

    def populate_choices(self):
        self.sport_id.choices = [(sport.id, sport.name) for sport in Sport.query.all()]
        self.country_id.choices = [(country.id, country.name) for country in Country.query.all()]
        self.athletes.choices = [(athlete.id, athlete.name) for athlete in Athlete.query.all()]
