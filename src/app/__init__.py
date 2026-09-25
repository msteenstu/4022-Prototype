'''
Author: Mckenna Steenbock
Description: This file initializes the Flask application,
database, and login handler.
Note: Code to populate the database was adapted from Steenbock (2026).
'''

from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask('Prototype Application')
app.secret_key = os.getenv('FLASK_SECRET_KEY')

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from app import models
with app.app_context():
    db.create_all()

    from app.setup import create_users, create_order
    create_users()
    create_order()

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User
@login_manager.user_loader
def load_user(id):
    try:
        return db.session.query(User).filter(User.id==id).one()
    except Exception:
        return None

from app import routes