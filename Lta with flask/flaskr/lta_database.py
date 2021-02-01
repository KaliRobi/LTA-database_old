import click
from flask import current_app, g
from flask.cli import with_appcontext
import psycopg2



# function to connect the database for data

def get_dt_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            current_app.config['RECORDS_DATABASE']
        )
        g.db.row_factory = psycopg2.row
    
    return g.db

# function to connect the database for data for the users
def get_users_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            current_app.config['USERS_DATABASE']
        )
        g.db.row_factory = psycopg2.row

# start up the database, authenticate too 
def start_dt_db():
    db =  get_dt_db()
    with current_app.open_resource('records.sql') as rec_dab:
        db.executescript(rec_dab.read().decode('UTF8'))

def start_users_db():
    db = get_users_db()
    with current_app.open_resource('users.sql') as users_dab:
        db.executescript(users_dab.read().decode('UTF8'))

#closes the conenction
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# cleans up after call

def init_app(app):
    app.teardown_appcontext(close_db)
    




