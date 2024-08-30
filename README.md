# Olympic Personnel Management System

This project is a web-based application built with Flask for managing Olympic athletes, sports, medals, and countries. The purpose of this system is to provide a streamlined way to handle and view data related to athletes, the events they compete in, the medals they win, and the countries they represent.

## Features

- **Athlete Management**: Add, update, and delete records of athletes.
- **Sport Management**: Manage different Olympic sports.
- **Medal Tracking**: Track the medals earned by athletes.
- **Country Representation**: Associate athletes with their respective countries.
- **Database Integration**: Uses Flask-SQLAlchemy and MySQL as the backend database.
- **Database Migrations**: Easily handle database schema changes using Flask-Migrate.

## Requirements

The project depends on the following libraries, which are listed in `requirements.txt`:

```plaintext
alembic==1.13.2
blinker==1.8.2
click==8.1.7
colorama==0.4.6
Flask==3.0.3
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
greenlet==3.0.3
itsdangerous==2.2.0
Jinja2==3.1.4
Mako==1.3.5
MarkupSafe==2.1.5
mysql-connector-python==9.0.0
SQLAlchemy==2.0.32
typing_extensions==4.12.2
Werkzeug==3.0.3
```

## Installation
1. Clone the repository:

```bash
git clone https://github.com/your-repo/olympic-management-system.git
cd olympic-management-system
```
2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install the dependencies:

```bash
pip install -r requirements.txt
```
4. Set up the database: Make sure you have MySQL installed and running. Update the database configuration in the app (typically in config.py).

```python
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
```
5. Run migrations to create the database schema:
```bash
flask db upgrade
```
6. Run the application:
```bash
flask run
```
The app will be available at http://127.0.0.1:5000/.

## Database Models
- Athlete: Stores information about athletes including name, country, and the sports they participate in.
- Sport: Manages the list of Olympic sports.
- Medal: Tracks the medals awarded to athletes (Gold, Silver, Bronze).
- Country: Represents countries participating in the Olympics.
