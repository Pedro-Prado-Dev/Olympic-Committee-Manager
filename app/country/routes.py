# app/country/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash
from flask.views import MethodView
from app import db
from app.country.model import Country
from app.country.form import CountryForm

country = Blueprint('country', __name__, url_prefix='/countries')


class CountryListView(MethodView):
    def get(self):
        countries = Country.query.all()
        return render_template('country/list.html', countries=countries)


class CountryCreateEditView(MethodView):
    def get(self, country_id=None):
        form = CountryForm()

        if country_id:
            country = Country.query.get_or_404(country_id)
            form.name.data = country.name
        else:
            country = None

        return render_template('country/create_edit.html', form=form, country=country)

    def post(self, country_id=None):
        form = CountryForm()

        if form.validate_on_submit():
            if country_id:
                country = Country.query.get_or_404(country_id)
                country.name = form.name.data
                flash('Country updated successfully!', 'success')
            else:
                country = Country(name=form.name.data)
                db.session.add(country)
                flash('Country created successfully!', 'success')

            db.session.commit()
            return redirect(url_for('country.country_list'))

        return render_template('country/create_edit.html', form=form)


class CountryDeleteView(MethodView):
    def post(self, country_id):
        country = Country.query.get_or_404(country_id)
        db.session.delete(country)
        db.session.commit()
        flash('Country deleted successfully!', 'danger')
        return redirect(url_for('country.country_list'))


# Registrar rotas
country.add_url_rule('/', view_func=CountryListView.as_view('country_list'))
country.add_url_rule('/create', view_func=CountryCreateEditView.as_view('country_create'))
country.add_url_rule('/<int:country_id>/edit', view_func=CountryCreateEditView.as_view('country_edit'))
country.add_url_rule('/<int:country_id>/delete', view_func=CountryDeleteView.as_view('country_delete'))
