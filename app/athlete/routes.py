from flask import Blueprint, render_template, redirect, url_for, flash, session
from flask.views import MethodView
from app import db
from app.athlete.model import Athlete
from app.athlete.form import AthleteForm

athlete = Blueprint('athlete', __name__, url_prefix='/')


class AthleteListView(MethodView):
    def get(self):
        athletes = Athlete.query.all()
        session['athlete_count'] = len(athletes)
        return render_template('athlete/index.html', athletes=athletes)


class AthleteCreateView(MethodView):
    def get(self):
        form = AthleteForm()
        return render_template('athlete/create_edit.html', form=form, title='Create Athlete')

    def post(self):
        form = AthleteForm()
        if form.validate_on_submit():
            athlete = Athlete(name=form.name.data, country_id=form.country_id.data, sport_id=form.sport_id.data)
            db.session.add(athlete)
            db.session.commit()
            flash('Athlete created successfully!', 'success')
            return redirect(url_for('athlete.athlete_list'))
        return render_template('athlete/create_edit.html', form=form, title='Create Athlete')


class AthleteEditView(MethodView):
    def get(self, athlete_id):
        athlete = Athlete.query.get_or_404(athlete_id)
        form = AthleteForm(obj=athlete)
        return render_template('athlete/create_edit.html', form=form, title='Edit Athlete')

    def post(self, athlete_id):
        athlete = Athlete.query.get_or_404(athlete_id)
        form = AthleteForm(obj=athlete)
        if form.validate_on_submit():
            athlete.name = form.name.data
            athlete.country_id = form.country_id.data
            athlete.sport_id = form.sport_id.data
            db.session.commit()
            flash('Athlete updated successfully!', 'success')
            return redirect(url_for('athlete.athlete_list'))
        return render_template('athlete/create_edit.html', form=form, title='Edit Athlete')


class AthleteDeleteView(MethodView):
    def post(self, athlete_id):
        athlete = Athlete.query.get_or_404(athlete_id)
        db.session.delete(athlete)
        db.session.commit()
        flash('Athlete deleted successfully!', 'success')
        return redirect(url_for('athlete.athlete_list'))


athlete.add_url_rule('/', view_func=AthleteListView.as_view('athlete_list'))
athlete.add_url_rule('/create', view_func=AthleteCreateView.as_view('athlete_create'))
athlete.add_url_rule('/edit/<int:athlete_id>', view_func=AthleteEditView.as_view('athlete_edit'))
athlete.add_url_rule('/delete/<int:athlete_id>', view_func=AthleteDeleteView.as_view('athlete_delete'))
