from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import STATIC_FOLDER
from config import TEMPLATE_FOLDER
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.athlete.routes import athlete
        from app.country.routes import country
        from app.medal.routes import medal
        from app.sport.routes import sport

        app.register_blueprint(athlete)
        app.register_blueprint(country)
        app.register_blueprint(medal)
        app.register_blueprint(sport)

        return app
