# app/country/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CountryForm(FlaskForm):
    name = StringField('Country Name', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Save')
