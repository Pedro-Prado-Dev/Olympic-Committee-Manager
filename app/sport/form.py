from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class SportForm(FlaskForm):
    name = StringField('Sport Name', validators=[DataRequired(), Length(max=100)])
    team_event = BooleanField('Is this a team event?')
    submit = SubmitField('Save')
