from flask import Blueprint, render_template, redirect, url_for, flash
from flask.views import MethodView
from app import db
from app.sport.model import Sport
from app.sport.form import SportForm

sport = Blueprint('sport', __name__, url_prefix='/sports')


class SportListView(MethodView):
    def get(self):
        sports = Sport.query.all()
        return render_template('sport/list.html', sports=sports)


class SportCreateEditView(MethodView):
    def get(self, sport_id=None):
        form = SportForm()

        if sport_id:
            sport = Sport.query.get_or_404(sport_id)
            form.name.data = sport.name
            form.team_event.data = sport.team_event
        else:
            sport = None

        return render_template('sport/create_edit.html', form=form, sport=sport)

    def post(self, sport_id=None):
        form = SportForm()

        if form.validate_on_submit():
            if sport_id:
                sport = Sport.query.get_or_404(sport_id)
                sport.name = form.name.data
                sport.team_event = form.team_event.data
                flash('Sport updated successfully!', 'success')
            else:
                sport = Sport(name=form.name.data, team_event=form.team_event.data)
                db.session.add(sport)
                flash('Sport created successfully!', 'success')

            db.session.commit()
            return redirect(url_for('sport.sport_list'))

        return render_template('sport/create_edit.html', form=form)


class SportDeleteView(MethodView):
    def post(self, sport_id):
        sport = Sport.query.get_or_404(sport_id)
        db.session.delete(sport)
        db.session.commit()
        flash('Sport deleted successfully!', 'danger')
        return redirect(url_for('sport.sport_list'))


sport.add_url_rule('/', view_func=SportListView.as_view('sport_list'))
sport.add_url_rule('/create', view_func=SportCreateEditView.as_view('sport_create'))
sport.add_url_rule('/<int:sport_id>/edit', view_func=SportCreateEditView.as_view('sport_edit'))
sport.add_url_rule('/<int:sport_id>/delete', view_func=SportDeleteView.as_view('sport_delete'))
