# app/medal/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask.views import MethodView
from app import db
from app.medal.model import Medal
from app.medal.form import MedalForm
from app.athlete.model import Athlete

medal = Blueprint('medal', __name__, url_prefix='/medals')


class MedalListView(MethodView):
    def get(self):
        medals = Medal.query.all()
        return render_template('medal/list.html', medals=medals)


class MedalCreateEditView(MethodView):
    def get(self, medal_id=None):
        form = MedalForm()
        form.populate_choices()

        if medal_id:
            medal = Medal.query.get_or_404(medal_id)
            form.type.data = medal.type
            form.event.data = medal.event
            form.sport_id.data = medal.sport_id
            form.country_id.data = medal.country_id
            form.athletes.data = [athlete.id for athlete in medal.athletes]
        else:
            medal = None

        return render_template('medal/create_edit.html', form=form, medal=medal)

    def post(self, medal_id=None):
        form = MedalForm()
        form.populate_choices()

        if form.validate_on_submit():
            if medal_id:
                medal = Medal.query.get_or_404(medal_id)
                flash('Medal updated successfully!', 'success')
            else:
                medal = Medal()
                db.session.add(medal)
                flash('Medal created successfully!', 'success')

            # Update the fields
            medal.type = form.type.data
            medal.event = form.event.data
            medal.sport_id = form.sport_id.data
            medal.country_id = form.country_id.data
            medal.athletes = Athlete.query.filter(Athlete.id.in_(form.athletes.data)).all()

            db.session.commit()
            return redirect(url_for('medal.medal_list'))

        return render_template('medal/create_edit.html', form=form)


class MedalDeleteView(MethodView):
    def post(self, medal_id):
        medal = Medal.query.get_or_404(medal_id)
        db.session.delete(medal)
        db.session.commit()
        flash('Medal deleted successfully!', 'danger')
        return redirect(url_for('medal.medal_list'))


medal.add_url_rule('/', view_func=MedalListView.as_view('medal_list'))
medal.add_url_rule('/create', view_func=MedalCreateEditView.as_view('medal_create'))
medal.add_url_rule('/<int:medal_id>/edit', view_func=MedalCreateEditView.as_view('medal_edit'))
medal.add_url_rule('/<int:medal_id>/delete', view_func=MedalDeleteView.as_view('medal_delete'))
