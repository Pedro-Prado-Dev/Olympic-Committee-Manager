import os
import sys

BASEDIR = os.path.dirname(os.path.abspath("run.py"))

STATIC_FOLDER = os.path.join(sys._MEIPASS, "static") if getattr(sys, "frozen", False) else "static"
TEMPLATE_FOLDER = os.path.join(sys._MEIPASS, "templates") if getattr(sys, "frozen", False) else "templates"

IMAGE_FOLDER = os.path.join("app", STATIC_FOLDER, "images")


class Config:
    FLASK_DEBUG = 1
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = "k\x8d-\xbd\xb9\x05\xeax\x92\xd9{H\xf0\x9c\xf9\xde\x91\xc6\xe6\xa8\x14\xf9\x89t"
    SQLALCHEMY_DATABASE_URI = \
        '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
            SGBD='mysql+mysqlconnector',
            usuario='root',
            senha='admin',
            servidor='localhost',
            database='olympic'
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'pedrohdppaiva@gmail.com'
    MAIL_PASSWORD = 'e n b k y v f w f j z i p b d v'
    MAIL_DEFAULT_SENDER = 'pedrohdppaiva@gmail.com'